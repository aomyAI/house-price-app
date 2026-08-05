import { useState } from "react";
import { predictPrice } from "../api/predictionClient";
import type { PredictionRequest, PredictionResponse } from "../types/prediction";

type PredictionForm = Omit<PredictionRequest, "carpet_area_sqft" | "floor_num" | "bathroom" | "balcony"> & {
  carpet_area_sqft: string;
  floor_num: string;
  bathroom: string;
  balcony: string;
};

const locations = [
  "mumbai",
  "navi-mumbai",
  "pune",
  "bangalore",
  "chennai",
  "hyderabad",
  "delhi",
  "other",
];

const furnishingOptions = ["Furnished", "Semi-Furnished", "Unfurnished"];
const transactionOptions = ["New Property", "Resale"];

export default function HomePage() {
  const [form, setForm] = useState<PredictionForm>({
    location: "mumbai",
    carpet_area_sqft: "0",
    floor_num: "1",
    bathroom: "1",
    balcony: "0",
    furnishing: "Semi-Furnished",
    transaction: "Resale",
    ownership: "Freehold",
    facing: "East",
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<PredictionResponse | null>(null);
  const [error, setError] = useState("");

  const handleChange = (key: keyof PredictionForm, value: string) => {
    setForm((current) => ({ ...current, [key]: value }));
  };

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();
    setError("");
    setResult(null);

    const carpetAreaValue = parseFloat(form.carpet_area_sqft);
    const floorValue = parseInt(form.floor_num, 10);
    const bathroomValue = parseInt(form.bathroom, 10);
    const balconyValue = parseInt(form.balcony, 10);

    if (Number.isNaN(carpetAreaValue) || carpetAreaValue <= 0) {
      setError("Carpet area must be greater than 0.");
      return;
    }

    const payload: PredictionRequest = {
      location: form.location,
      carpet_area_sqft: carpetAreaValue,
      floor_num: floorValue,
      bathroom: bathroomValue,
      balcony: balconyValue,
      furnishing: form.furnishing,
      transaction: form.transaction,
      ownership: form.ownership,
      facing: form.facing,
    };

    setLoading(true);
    try {
      const response = await predictPrice(payload);
      setResult(response);
    } catch (err) {
      setError((err as Error).message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main style={{ padding: 24, maxWidth: 640, margin: "0 auto" }}>
      <h1>House Price Prediction</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Location
          <select
            value={form.location}
            onChange={(event) => handleChange("location", event.target.value)}
          >
            {locations.map((location) => (
              <option key={location} value={location}>
                {location}
              </option>
            ))}
          </select>
        </label>

        <label>
          Carpet Area (sqft)
          <input
            type="number"
            value={form.carpet_area_sqft}
            onChange={(event) => handleChange("carpet_area_sqft", event.target.value)}
            min={0}
          />
        </label>

        <label>
          Floor Number
          <input
            type="number"
            value={form.floor_num}
            onChange={(event) => handleChange("floor_num", event.target.value)}
            min={1}
          />
        </label>

        <label>
          Bathrooms
          <input
            type="number"
            value={form.bathroom}
            onChange={(event) => handleChange("bathroom", event.target.value)}
            min={1}
          />
        </label>

        <label>
          Balconies
          <input
            type="number"
            value={form.balcony}
            onChange={(event) => handleChange("balcony", event.target.value)}
            min={0}
          />
        </label>

        <label>
          Furnishing
          <select
            value={form.furnishing}
            onChange={(event) => handleChange("furnishing", event.target.value)}
          >
            {furnishingOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

        <label>
          Transaction
          <select
            value={form.transaction}
            onChange={(event) => handleChange("transaction", event.target.value)}
          >
            {transactionOptions.map((option) => (
              <option key={option} value={option}>
                {option}
              </option>
            ))}
          </select>
        </label>

        <label>
          Ownership
          <input
            type="text"
            value={form.ownership}
            onChange={(event) => handleChange("ownership", event.target.value)}
          />
        </label>

        <label>
          Facing
          <input
            type="text"
            value={form.facing}
            onChange={(event) => handleChange("facing", event.target.value)}
          />
        </label>

        <button type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Predict Price"}
        </button>
      </form>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <section style={{ marginTop: 24 }}>
          <h2>Prediction Result</h2>
          <p>
            Predicted price: <strong>{result.predicted_price.toLocaleString()}</strong>
          </p>
        </section>
      )}
    </main>
  );
}
