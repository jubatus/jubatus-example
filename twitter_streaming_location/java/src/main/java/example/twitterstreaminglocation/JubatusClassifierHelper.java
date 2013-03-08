package example.twitterstreaminglocation;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import us.jubat.classifier.Datum;
import us.jubat.classifier.TupleStringDatum;
import us.jubat.classifier.TupleStringDouble;
import us.jubat.classifier.TupleStringString;

public class JubatusClassifierHelper {
	public static Datum newDatum() {
		Datum d = new Datum();
		d.string_values = new ArrayList<TupleStringString>();
		d.num_values = new ArrayList<TupleStringDouble>();
		return d;
	}

	public static TupleStringString newTupleStringString(String key,
			String value) {
		TupleStringString t = new TupleStringString();
		t.first = key;
		t.second = value;
		return t;
	}

	public static TupleStringDouble newTupleStringDouble(String key,
			double value) {
		TupleStringDouble t = new TupleStringDouble();
		t.first = key;
		t.second = value;
		return t;
	}

	public static TupleStringDatum newTupleStringDatum(String key, Datum value) {
		TupleStringDatum t = new TupleStringDatum();
		t.first = key;
		t.second = value;
		return t;
	}

	public static <T> List<T> list(T... objects) {
		return Arrays.asList(objects);
	}
}
