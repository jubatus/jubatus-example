package us.jubat.example.slot;

import ca.szc.configparser.Ini;
import ca.szc.configparser.exceptions.IniParserException;
import org.msgpack.rpc.loop.EventLoop;
import us.jubat.bandit.ArmInfo;
import us.jubat.bandit.BanditClient;

import java.io.IOException;
import java.net.UnknownHostException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

public class Slot {
    public static final String HOST = "127.0.0.1";
    public static final int PORT = 9199;
    public static final String NAME = "bandit";
    public static final int CLIENT_TIMEOUT = 10;

    public static final String SLOT_CONFIG_FILE_PATH = "../config/slot.conf";
    public static final String PLAYER = "player_A";
    private BanditClient client;


    private int ITERATION_DEFAULT = 1000;

    private Map<String , SlotMachine> slotMap;
    private int iteration;


    public Slot() {
        try {
            //load config
            Path input = Paths.get(SLOT_CONFIG_FILE_PATH);

            Ini ini = new Ini().read(input);
            Map<String, Map<String, String>> sections = ini.getSections();

            Map<String, String> commonSection = sections.get("common");
            Map<String, String> slotsSection = sections.get("slots");
            String iterationString;

            //iteration
            if(commonSection != null && (iterationString = commonSection.get("iteration")) != null){
                iteration = Integer.parseInt(iterationString);
            }else{
                iteration = ITERATION_DEFAULT;
            }

            //slots config
            if(slotsSection == null || slotsSection.size() <=0) {
                System.out.println("Invalid Config !");
                return ;
            }

            slotMap = new HashMap<String , SlotMachine>();
            client = new BanditClient(HOST, PORT, NAME, CLIENT_TIMEOUT);

            for(Map.Entry<String,String> slotConfig : slotsSection.entrySet()) {
                String arm = slotConfig.getKey();
                String config = slotConfig.getValue();
                String[] tokens = config.split(",");

                SlotMachine machine = new SlotMachine(Float.parseFloat(tokens[0]) , Float.parseFloat(tokens[1]) , Float.parseFloat(tokens[2]));
                slotMap.put(arm,machine);
                client.registerArm(arm);
            }

        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IniParserException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }




    public void start() throws Exception {

        try {
            //trial
            client.reset(PLAYER);
            float cumulativeReward = 0;

            for(int i=0;i< iteration;i++) {
                String arm = client.selectArm(PLAYER);
                SlotMachine machine = slotMap.get(arm);
                float reward = machine.generateReward();
                client.registerReward(PLAYER , arm , reward);

                cumulativeReward += reward;
            }

            //result
            System.out.println(String.format("cumulative reward is %.2f" , cumulativeReward));
            Map<String, ArmInfo> armInfoMap = client.getArmInfo(PLAYER);

            System.out.println("slot frequencies are:");
            for(Map.Entry<String, ArmInfo> arm :armInfoMap.entrySet() ){
                System.out.println(arm.getKey() + " => "+ arm.getValue().trialCount);
            }

        } finally {
            client.getClient().close();
        }
    }

    public static void main(String[] args) throws Exception {
        try {
            new Slot().start();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // msgpack-rpc-java does not stop the EventLoop automatically
            EventLoop.defaultEventLoop().shutdown();
            EventLoop.setDefaultEventLoop(null);
        }
    }
}
