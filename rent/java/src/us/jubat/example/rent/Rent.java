package us.jubat.example.rent;

import com.opencsv.CSVParser;
import com.opencsv.CSVReader;
import org.msgpack.rpc.loop.EventLoop;
import org.yaml.snakeyaml.Yaml;
import us.jubat.common.Datum;
import us.jubat.regression.RegressionClient;
import us.jubat.regression.ScoredDatum;

import java.io.*;
import java.net.UnknownHostException;
import java.util.*;

public class Rent {
    public static final String HOST = "127.0.0.1";
    public static final int PORT = 9199;
    public static final String NAME = "rent";
    public static final int CLIENT_TIMEOUT = 10;
    public static final String RENT_TRAIN_CSV_FILE_PATH = "../dat/rent-data.csv";
    public static final String RENT_TEST_YML_FILE_PATH = "../dat/myhome.yml";

    private RegressionClient client;

    private List<ScoredDatum> loadedDatas = new ArrayList<ScoredDatum>();
    private String[] csvHeader = {"rent","distance", "space", "age", "stair" , "aspect"};
    private List<ScoredDatum> trainDatas;
    private List<Datum> testDatas;

    public Rent() {
        try {
            //Connect to jubaregression Server
            client = new RegressionClient(HOST, PORT, NAME, CLIENT_TIMEOUT);
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }

    }

    private void load() throws IOException {

        //Load CSV File for Train
        FileReader fr = new FileReader(RENT_TRAIN_CSV_FILE_PATH);
        CSVReader reader = new CSVReader(fr , 5 , new CSVParser());

        String[] line;
        while ((line = reader.readNext()) != null) {
            Datum datum = new Datum()
                    .addNumber(csvHeader[1], Double.parseDouble(line[1]))
                    .addNumber(csvHeader[2], Double.parseDouble(line[2]))
                    .addNumber(csvHeader[3], Double.parseDouble(line[3]))
                    .addNumber(csvHeader[4], Double.parseDouble(line[4]))
                    .addString(csvHeader[5], line[5]);

            loadedDatas.add(new ScoredDatum(Float.parseFloat(line[0]), datum));
        }
        trainDatas = loadedDatas;

        reader.close();
        fr.close();

        //Load Yaml File for Prediction
        Yaml yaml = new Yaml();

        InputStream input = new FileInputStream(new File(RENT_TEST_YML_FILE_PATH));

        MyHome myHome = yaml.loadAs(input , MyHome.class);
        Datum datum = new Datum()
                .addNumber(csvHeader[1], myHome.getDistance())
                .addNumber(csvHeader[2], myHome.getSpace())
                .addNumber(csvHeader[3], myHome.getAge())
                .addNumber(csvHeader[4], myHome.getStair())
                .addString(csvHeader[5], myHome.getAspect());

        Datum[] testDataArray = {datum};
        testDatas = Arrays.asList(testDataArray);

        input.close();

    }


    public void start() throws Exception {

        try {
            //Initialize
            load();

            //Train
            client.train(trainDatas);

            //Analyze
            List<Float> resultList = client.estimate(testDatas);

            //Result
            System.out.println(String.format("物件の家賃予測: 月%.1f万円" , resultList.get(0)));

        } finally {
            client.getClient().close();
        }
    }

    public static void main(String[] args) throws Exception {
        try {
            new Rent().start();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // msgpack-rpc-java does not stop the EventLoop automatically
            EventLoop.defaultEventLoop().shutdown();
            EventLoop.setDefaultEventLoop(null);
        }
    }
}
