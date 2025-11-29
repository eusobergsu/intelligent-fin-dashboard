// frontend/src/services/api.js
const API_BASE = ""; // proxy is set in package.json, so leave empty

async function apiGet(path) {
  try {
    const res = await fetch(`${API_BASE}${path}`);
    if (!res.ok) throw new Error(`API error ${res.status}`);
    return await res.json();
  } catch (err) {
    console.error("API fetch error:", err);
    return { error: err.message };
  }
}

export const MarketAPI = {
  summary: () => apiGet("/market/summary"),
  history: (symbol, days = 7) => apiGet(`/market/history/${symbol}?days=${days}`)
};

export const CryptoAPI = {
  summary: () => apiGet("/crypto/summary"),
  ticker: (symbol, interval = "1h") =>
    apiGet(`/crypto/ticker/${symbol}?interval=${interval}`)
};
