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
import us.jubat.recommender.Datum;
import us.jubat.recommender.TupleStringDouble;
import us.jubat.recommender.TupleStringString;

public class Update {
  public static final String HOST = "127.0.0.1";
  public static final int PORT = 9199;
  public static final String NAME = "ML";
  public static final String Data_PATH = "../dat/ml-100k/u.data";

  public void start() throws Exception {
          // 1. Connect to Jubatus Server
          RecommenderClient client = new RecommenderClient(HOST, PORT, 5);

          // 2. Prepare training data
          try{
                  File csv = new File(Data_PATH); // read data file

                  BufferedReader br = new BufferedReader(new FileReader(csv));

                  String line = "";

                  // read the file line by line til the end
                  while ((line = br.readLine()) != null) {


                    Datum datum = new Datum();
                    datum.string_values = new ArrayList<TupleStringString>();
                    datum.num_values = new ArrayList<TupleStringDouble>();
                    // split the line for items
                    String[] strAry = line.split("\t");
  
                    try{
                       TupleStringDouble data = new TupleStringDouble();
                       data.first = strAry[1];
                       data.second = Double.parseDouble(strAry[2]);
                       datum.num_values.add(data);
                       }catch(NumberFormatException e){
                    }

                    // 3. training the model
                    client.update_row(NAME, strAry[0], datum);
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
