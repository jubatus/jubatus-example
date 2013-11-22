package us.jubat.example.ml;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import us.jubat.recommender.RecommenderClient;
import us.jubat.common.Datum;

public class Update {
  public static final String HOST = "127.0.0.1";
  public static final int PORT = 9199;
  public static final String NAME = "ML";
  public static final String Data_PATH = "../dat/ml-100k/u.data";

  public void start() throws Exception {
          // 1. Connect to Jubatus Server
          RecommenderClient client = new RecommenderClient(HOST, PORT, NAME, 5);

          // 2. Prepare training data
          try{
                  File csv = new File(Data_PATH); // read data file

                  BufferedReader br = new BufferedReader(new FileReader(csv));

                  String line = "";

                  // read the file line by line til the end
                  while ((line = br.readLine()) != null) {


                    Datum datum = new Datum();
                    // split the line for items
                    String[] strAry = line.split("\t");
  
                    try{
                       datum.addNumber(strAry[1], Double.parseDouble(strAry[2]));
                    }catch(NumberFormatException e){
                    }

                    // 3. training the model
                    client.updateRow(strAry[0], datum);
                  }
                br.close();
          }catch(FileNotFoundException e){
                    // capture exception when creating file object
                   e.printStackTrace();
          }catch(IOException e) {
                   // capture exception when close BufferedReader object
                    e.printStackTrace();
          }
          return;
  }

  //Main method
public static void main(String[] args) throws Exception {
          new Update().start();
          System.exit(0);
   }
}
