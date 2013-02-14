package us.jubat.example.gender;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import us.jubat.classifier.ClassifierClient;
import us.jubat.classifier.Datum;
import us.jubat.classifier.EstimateResult;
import us.jubat.classifier.TupleStringDatum;
import us.jubat.classifier.TupleStringDouble;
import us.jubat.classifier.TupleStringString;

public class GenderMain {

	private static TupleStringString makeStringTuple(String first, String second) {
		TupleStringString t = new TupleStringString();
		t.first = first;
		t.second = second;
		return t;
	}

	private static TupleStringDouble makeDoubleTuple(String first, double second) {
		TupleStringDouble t = new TupleStringDouble();
		t.first = first;
		t.second = second;
		return t;
	}

	private static Datum makeDatum(String hair, String top, String bottom,
			double height) {
		Datum d = new Datum();
		d.string_values = new ArrayList<TupleStringString>();
		d.string_values.add(makeStringTuple("hair", hair));
		d.string_values.add(makeStringTuple("top", top));
		d.string_values.add(makeStringTuple("bottom", bottom));

		d.num_values = new ArrayList<TupleStringDouble>();
		d.num_values.add(makeDoubleTuple("height", height));
		return d;
	}

	private static TupleStringDatum makeTrainDatum(String label, String hair,
			String top, String bottom, double height) {
		TupleStringDatum t = new TupleStringDatum();
		t.first = label;
		t.second = makeDatum(hair, top, bottom, height);
		return t;
	}

	public static void main(String[] args) throws Exception {
		String host = "127.0.0.1";
		int port = 9199;
		String name = "test";

		ClassifierClient client = new ClassifierClient(host, port, 1.0);

		TupleStringDatum[] trainData = { //
		makeTrainDatum("male", "short", "sweater", "jeans", 1.70),
				makeTrainDatum("female", "long", "shirt", "skirt", 1.56),
				makeTrainDatum("male", "short", "jacket", "chino", 1.65),
				makeTrainDatum("female", "short", "T shirt", "jeans", 1.72),
				makeTrainDatum("male", "long", "T shirt", "jeans", 1.82),
				makeTrainDatum("female", "long", "jacket", "skirt", 1.43),
				// makeTrainDatum("male", "short", "jacket", "jeans", 1.76),
				// makeTrainDatum("female", "long", "sweater", "skirt", 1.52),
				};

		client.train(name, Arrays.asList(trainData));

		Datum[] testData = { //
		makeDatum("short", "T shirt", "jeans", 1.81),
				makeDatum("long", "shirt", "skirt", 1.50), };

		List<List<EstimateResult>> results = client.classify(name,
				Arrays.asList(testData));

		for (List<EstimateResult> result : results) {
			for (EstimateResult r : result) {
				System.out.printf("%s %f\n", r.label, r.score);
			}
			System.out.println();
		}
		
		System.exit(0);
	}
}
