package us.jubat.example.ml;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import us.jubat.recommender.RecommenderClient;
import us.jubat.recommender.TupleStringFloat;

public class Analyze {
  public static final String HOST = "127.0.0.1";
  public static final int PORT = 9199;
  public static final String NAME = "ML";

  public void start() throws Exception {
          // 1. Connect to Jubatus Server
          RecommenderClient client = new RecommenderClient(HOST, PORT, 5);

          // 2. Get the recommended results for every user
          List<TupleStringFloat> rec = new ArrayList<TupleStringFloat>(); 
          for (int i=0; i<=943; i++) {
            rec = client.similar_row_from_id("movie_len", Integer.toString(i), 10);                         
         //3. ouput result
            System.out.print("audience " + Integer.toString(i) + " is similar to : " );
            for (int j=0; j<10; j++){
                System.out.print(rec.get(j).first + " ");
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
