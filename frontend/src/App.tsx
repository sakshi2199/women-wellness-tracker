import { useState, useEffect } from "react";

function App() {
  const [status, setStatus] = useState("loading...");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((response) => response.json())
      .then((data) => setStatus(data.status));
  }, []);

  return (
    <div>
      <h1>Wellness Tracker</h1>
      <p>Backend status: {status}</p>
    </div>
  );
}

export default App;
