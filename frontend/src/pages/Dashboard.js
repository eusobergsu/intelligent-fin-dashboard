// frontend/src/pages/Dashboard.js
import React, { useEffect, useState } from "react";
import { MarketAPI, CryptoAPI } from "../services/api";

export default function Dashboard() {
  const [market, setMarket] = useState(null);
  const [crypto, setCrypto] = useState(null);

  useEffect(() => {
    async function load() {
      const [m, c] = await Promise.all([MarketAPI.summary(), CryptoAPI.summary()]);
      setMarket(m);
      setCrypto(c);
    }
    load();
  }, []);

  return (
    <div style={{ padding: 20 }}>
      <h1>Intelligent Financial Dashboard — Demo</h1>

      <section>
        <h2>Market Summary</h2>
        <pre>{market ? JSON.stringify(market, null, 2) : "Loading..."}</pre>
      </section>

      <section>
        <h2>Crypto Summary</h2>
        <pre>{crypto ? JSON.stringify(crypto, null, 2) : "Loading..."}</pre>
      </section>
    </div>
  );
}
