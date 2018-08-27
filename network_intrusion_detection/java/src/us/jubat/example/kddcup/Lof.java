package us.jubat.example.kddcup;

import us.jubat.anomaly.AnomalyClient;
import us.jubat.anomaly.IdWithScore;
import us.jubat.common.Datum;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Lof {
    public static final String HOST = "127.0.0.1";
    public static final int PORT = 9199;
    public static final String NAME = "anom_kddcup";
    public static final String FILE_PATH = "../";
    public static final String TEXT_NAME = "kddcup.data_10_percent.txt";

    // TEXTのカラム名定義
    public static String[] TEXT_COLUMN = {
            "duration",
            "protocol_type",
            "service",
            "flag",
            "src_bytes",
            "dst_bytes",
            "land",
            "wrong_fragment",
            "urgent",
            "hot",
            "num_failed_logins",
            "logged_in",
            "num_compromised",
            "root_shell",
            "su_attempted",
            "num_root",
            "num_file_creations",
            "num_shells",
            "num_access_files",
            "num_outbound_cmds",
            "is_host_login",
            "is_guest_login",
            "count",
            "srv_count",
            "serror_rate",
            "srv_serror_rate",
            "rerror_rate",
            "srv_rerror_rate",
            "same_srv_rate",
            "diff_srv_rate",
            "srv_diff_host_rate",
            "dst_host_count",
            "dst_host_srv_count",
            "dst_host_same_srv_rate",
            "dst_host_diff_srv_rate",
            "dst_host_same_src_port_rate",
            "dst_host_srv_diff_host_rate",
            "dst_host_serror_rate",
            "dst_host_srv_serror_rate",
            "dst_host_rerror_rate",
            "dst_host_srv_rerror_rate",
            "label"
    };

    // String型の項目
    public static String[] STRING_COLUMN = {
            "protocol_type",
            "service",
            "flag",
            "land",
            "logged_in",
            "is_host_login",
            "is_guest_login"
    };

    // Double型の項目
    public static String[] DOUBLE_COLUMN = {
            "duration",
            "src_bytes",
            "dst_bytes",
            "wrong_fragment",
            "urgent",
            "hot",
            "num_failed_logins",
            "num_compromised",
            "root_shell",
            "su_attempted",
            "num_root",
            "num_file_creations",
            "num_shells",
            "num_access_files",
            "num_outbound_cmds",
            "count",
            "srv_count",
            "serror_rate",
            "srv_serror_rate",
            "rerror_rate",
            "srv_rerror_rate",
            "same_srv_rate",
            "diff_srv_rate",
            "srv_diff_host_rate",
            "dst_host_count",
            "dst_host_srv_count",
            "dst_host_same_srv_rate",
            "dst_host_same_src_port_rate",
            "dst_host_diff_srv_rate",
            "dst_host_srv_diff_host_rate",
            "dst_host_serror_rate",
            "dst_host_srv_serror_rate",
            "dst_host_rerror_rate",
            "dst_host_srv_rerror_rate"
    };

    public void execute() throws Exception {
        // 1. Jubatus Serverへの接続設定
        AnomalyClient client = new AnomalyClient(HOST, PORT , NAME, 5);

        // 2. 学習用データの準備
        Datum datum = null;
        IdWithScore result = null;

        try {
            BufferedReader br = new BufferedReader(new FileReader(new File(FILE_PATH , TEXT_NAME)));

            List<String> strList = new ArrayList<String>();
            List<String> doubleList = new ArrayList<String>();

            String line = "";

            // 最終行までループでまわし、1行ずつ読み込む
            while ((line = br.readLine()) != null) {
                strList.clear();
                doubleList.clear();

                // 1行をデータの要素に分割
                String[] strAry = line.split(",");

                // StringとDoubleの項目ごとにListを作成
                for (int i = 0; i < strAry.length; i++) {
                    if (Arrays.toString(STRING_COLUMN).contains(TEXT_COLUMN[i])) {
                        strList.add(strAry[i]);
                    } else if (Arrays.toString(DOUBLE_COLUMN).contains(TEXT_COLUMN[i])) {
                        doubleList.add(strAry[i]);
                    }
                }
                // datumを作成
                datum = makeDatum(strList, doubleList);

                // 3. データの学習（学習モデルの更新）
                result = client.add(datum);

                // 4. 結果の出力
                if (!(Double.isInfinite(result.score)) && result.score != 1.0) {
                    System.out.print("('" + result.id + "', " + result.score + ") " + strAry[strAry.length - 1] + "\n");
                }
            }
            br.close();

        } catch (FileNotFoundException e) {
            // Fileオブジェクト生成時の例外捕捉
            e.printStackTrace();
        } catch (IOException e) {
            // BufferedReaderオブジェクトのクローズ時の例外捕捉
            e.printStackTrace();
        }
        return;
    }


    // Datumを指定された名称で、リスト分作成
    private Datum makeDatum(List<String> strList, List<String> doubleList) {

        Datum datum = new Datum();

        for (int i = 0; i < strList.size(); i++) {
            datum.addString(STRING_COLUMN[i],strList.get(i));
        }

        try {
            for (int i = 0; i < doubleList.size(); i++) {
                datum.addNumber(DOUBLE_COLUMN[i],Double.parseDouble(doubleList.get(i)));
            }
        } catch (NumberFormatException e) {
            e.printStackTrace();
            return null;
        }

        return datum;
    }

    // メインメソッド
    public static void main(String[] args) throws Exception {

        new Lof().execute();
        System.exit(0);
    }
}
