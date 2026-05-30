import { useEffect, useState } from "react";
import API from "../services/api";
import InsightsCard from "../components/InsightsCard";

function cleanText(text) {
  if (!text) return "";

  return text
    .replaceAll("**", "")
    .replaceAll("###", "")
    .replaceAll("\\n", "\n");
}

function InsightsPage({ insights }) {
  const [crewSummary, setCrewSummary] = useState(null);

  useEffect(() => {
    API.get("/crew-ai/summary")
      .then((res) => setCrewSummary(res.data.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <>
      <h2>🤖 AI Insights</h2>

      {crewSummary && (
        <div
          style={{
            background: "#132238",
            padding: "25px",
            borderRadius: "12px",
            marginBottom: "25px",
            color: "white",
            border: "1px solid #2f4f75",
          }}
        >
          <h3>🧠 CrewAI Multi-Agent Decision Support System</h3>

          <p>🟢 Powered by CrewAI Multi-Agent Framework + Mistral LLM</p>

          <p>
            <b>Framework:</b> {crewSummary.framework}
          </p>

          <p>
            <b>Model:</b> {crewSummary.model}
          </p>

          <hr />

          <h3>Transit Operations Summary</h3>

          <h4>Current Performance</h4>

          <p>
            <b>Reliability:</b> {crewSummary.metrics.reliability_score}%
          </p>

          <p>
            <b>Delay Frequency:</b>{" "}
            {crewSummary.metrics.delay_frequency_percent}%
          </p>

          <p>
            <b>Peak Hour:</b>{" "}
            {crewSummary.metrics.peak_disruption_hour}
          </p>

          <hr />

          <h4>Key Findings</h4>

          <ul style={{ textAlign: "left", display: "inline-block" }}>
            <li>Route 4 is the worst performing route.</li>
            <li>Route 2 is the second worst performer.</li>
            <li>Peak congestion occurs around 8 AM.</li>
          </ul>

          <hr />

          <h4>Recommendations</h4>

          <ul style={{ textAlign: "left", display: "inline-block" }}>
            <li>Increase service frequency during peak periods.</li>
            <li>Implement traffic signal priority where possible.</li>
            <li>Monitor Route 4 for operational improvements.</li>
          </ul>

          <hr />

          <h4>LLM Analysis</h4>

<p
  style={{
    whiteSpace: "pre-line",
    lineHeight: "1.8",
    textAlign: "left",
    padding: "0 20px",
  }}
>
  {cleanText(crewSummary.summary)}
</p>
        </div>
      )}

      <h3>📊 Rule-Based Operational Insights</h3>

      {insights.map((item, index) => (
        <InsightsCard key={index} item={item} />
      ))}
    </>
  );
}

export default InsightsPage;