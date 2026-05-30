function InsightsCard({ item }) {
  const isAction = item.title === "Recommended Action";

  return (
    <div
      style={{
        marginBottom: "25px",
        padding: "25px",
        borderRadius: "12px",
        background: isAction ? "#17351d" : "#111827",
        border: isAction
          ? "2px solid #4CAF50"
          : "1px solid #333",
      }}
    >
      <h3
        style={{
          color: isAction ? "#4CAF50" : "white",
        }}
      >
        {item.title}
      </h3>

      <p>
        <b>Insight:</b> {item.message}
      </p>

      <p style={{ color: "#cccccc" }}>
        <b>Why:</b> {item.explanation}
      </p>

      {item.impact && (
        <div>
          <b>Impact:</b>

          <ul>
            {item.impact.map((impact, index) => (
              <li key={index}>{impact}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default InsightsCard;