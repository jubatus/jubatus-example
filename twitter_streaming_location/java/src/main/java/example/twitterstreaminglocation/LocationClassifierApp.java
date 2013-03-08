package example.twitterstreaminglocation;

import static example.twitterstreaminglocation.JubatusClassifierHelper.list;
import static example.twitterstreaminglocation.JubatusClassifierHelper.newDatum;
import static example.twitterstreaminglocation.JubatusClassifierHelper.newTupleStringString;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

import us.jubat.classifier.ClassifierClient;
import us.jubat.classifier.Datum;
import us.jubat.classifier.EstimateResult;

public class LocationClassifierApp {
	// Jubatus Configuration
	private String host = "localhost";
	private int port = 9199;
	// required only when using distributed mode
	private String instanceName = "";

	public void estimateLocationFor(String sentence) throws Exception {
		ClassifierClient client = new ClassifierClient(host, port, 10);

		// Create datum for Jubatus
		Datum d = newDatum();
		d.string_values.add(newTupleStringString("text", sentence));

		// Send estimation query to Jubatus
		List<List<EstimateResult>> result = client.classify(instanceName,
				list(d));
		if (result.get(0).size() > 0) {
			List<EstimateResult> est = result.get(0);
			Collections.sort(est,
					Collections.reverseOrder(new Comparator<EstimateResult>() {
						public int compare(EstimateResult o1, EstimateResult o2) {
							return (int) (o1.score - o2.score);
						}
					}));
			System.out.println("Estimated Location for " + sentence + ":");
			for (EstimateResult e : est) {
				System.out.println("  " + e.label + " (" + e.score + ")");
			}
		} else {
			// No estimation results; maybe we haven't trained enough
			System.out.println("No estimation results available.");
			System.out.println("Train more tweets or try using another text.");
		}
	}

	public void run() throws Exception {
		BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
		String line;
		while (true) {
			System.out.print("Sentence> ");
			line = r.readLine();
			if (line == null || line.equals("")) {
				break;
			}
			estimateLocationFor(line);
		}
	}

	public static void main(String[] args) throws Exception {
		new LocationClassifierApp().run();
		System.exit(0);
	}
}
