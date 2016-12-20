package us.jubat.example.ml;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import us.jubat.recommender.RecommenderClient;
import us.jubat.recommender.IdWithScore;

public class Analyze {
  public static final String HOST = "127.0.0.1";
  public static final int PORT = 9199;
  public static final String NAME = "ML";

  public void start() throws Exception {
          // 1. Connect to Jubatus Server
          RecommenderClient client = new RecommenderClient(HOST, PORT, NAME, 5);

          // 2. Get the recommended results for every user
          for (int i=1; i<=943; i++) {
            List<IdWithScore> rec = client.similarRowFromId(Integer.toString(i), 10);
         //3. ouput result
            System.out.print("audience " + Integer.toString(i) + " is similar to : " );
            for (int j=0; j<10; j++){
                System.out.print(rec.get(j).id + " ");
            }
            System.out.println();
          }
          return;
  }

  //Main method
public static void main(String[] args) throws Exception {
          new Analyze().start();
          System.exit(0);
   }
}
