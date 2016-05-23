package us.jubat.example.trivial_stat;

import com.opencsv.CSVParser;
import com.opencsv.CSVReader;
import org.msgpack.rpc.loop.EventLoop;
import us.jubat.stat.StatClient;

import java.io.*;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.List;

public class TrivialStat {
    public static final String HOST = "127.0.0.1";
    public static final int PORT = 9199;
    public static final String NAME = "trivial_stat";
    public static final int CLIENT_TIMEOUT = 10;
    public static final String TRIVIAL_TRAIN_CSV_FILE_PATH = "../dat/fruit.csv";
    private StatClient client;

    private List<String[]> loadedDatas = new ArrayList<String[]>();
    private String[] csvHeader = {"fruit", "diameter", "weight", "price"};
    private String[] fruits = {"orange", "apple","melon"};
    private String[] items = {"diameter", "weight", "price"};
    private List<String[]> trainDatas;

    public TrivialStat() {
        try {
            client = new StatClient(HOST, PORT, NAME, CLIENT_TIMEOUT);
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }

    private void load() throws IOException {
        //Load fruits data .
        FileReader fr = new FileReader(TRIVIAL_TRAIN_CSV_FILE_PATH);
        CSVReader reader = new CSVReader(fr);

        String[] line;
        while ((line = reader.readNext()) != null) {
            loadedDatas.add(line);
        }
        trainDatas = loadedDatas;

        reader.close();
        fr.close();
    }

    public void start() throws Exception {

        try {
            load();

            //push datas
            for(String[] trainData:trainDatas) {
                //input Diameter
                client.push(trainData[0] + csvHeader[1] , Double.parseDouble(trainData[1]));

                //input Weight
                client.push(trainData[0] + csvHeader[2] , Double.parseDouble(trainData[2]));

                //input Price
                client.push(trainData[0] + csvHeader[3] , Double.parseDouble(trainData[3]));
            }

            //display current result.
            for(String fruit:fruits){
                for (String item : items) {
                    System.out.println("sum :"+ fruit + item+ " " + client.sum(fruit + item));
                    System.out.println("sdv :"+ fruit + item+ " " + client.stddev(fruit + item));
                    System.out.println("max :"+ fruit + item+ " " + client.max(fruit + item));
                    System.out.println("min :"+ fruit + item+ " " + client.min(fruit + item));
                    System.out.println("ent :"+ fruit + item+ " " + client.entropy(fruit + item));
                    System.out.println("mmt :"+ fruit + item+ " " + client.moment(fruit + item, 1, 0.0));
                }
            }

        } finally {
            client.getClient().close();
        }
    }

    public static void main(String[] args) throws Exception {
        try {
            new TrivialStat().start();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // msgpack-rpc-java does not stop the EventLoop automatically
            EventLoop.defaultEventLoop().shutdown();
            EventLoop.setDefaultEventLoop(null);
        }
    }
}
