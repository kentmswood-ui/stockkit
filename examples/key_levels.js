/**
 * StockKit API Example: Support & Resistance Levels
 * https://stockkit.net
 */
async function getKeyLevels(symbol, market = 'US') {
  const url = `https://stockkit.net/api/levels?symbol=${symbol}&market=${market}`;
  const res = await fetch(url);
  return res.json();
}

// Usage
getKeyLevels('AAPL', 'US').then(data => {
  console.log('AAPL Key Levels:', JSON.stringify(data, null, 2));
});
