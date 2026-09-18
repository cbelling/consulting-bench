(function () {
  const data = window.LEADERBOARD;
  if (!data) {
    document.body.insertAdjacentHTML("afterbegin", "<p>Missing website/data.js</p>");
    return;
  }

  const money = (n) => (n == null || Number.isNaN(n) ? "—" : `$${Number(n).toFixed(2)}`);
  const pct = (n) => (n == null ? "—" : `${Math.round(n * 100)}%`);
  const when = data.updated_at ? new Date(data.updated_at).toISOString().slice(0, 16) + "Z" : "";

  document.getElementById("updated").textContent =
    `${data.set} · ${data.n_tasks} tasks · ${data.agent} on ${data.environment} · updated ${when}`;

  const est = data.cost_estimate || {};
  document.getElementById("cost-copy").textContent =
    `${est.notes || ""} Expected about $${est.four_flagships_expected_usd}; upper about $${est.four_flagships_upper_usd}. ` +
    `Baseline tokens: ${(est.baseline_tokens || {}).input} in / ${(est.baseline_tokens || {}).output} out.`;

  const costRows = (data.models || []).map((m) => {
    const actual = m.status === "complete" ? money(m.cost_usd) : "pending";
    return `<tr>
      <td>${m.display}</td>
      <td class="num">${m.list_price_usd_per_m.input} / ${m.list_price_usd_per_m.output}</td>
      <td class="num">${money(m.estimated_llm_usd)}</td>
      <td class="num">${money(m.estimated_llm_usd_2x_output)}</td>
      <td class="num">${actual}</td>
    </tr>`;
  }).join("");
  document.getElementById("cost-table").innerHTML = `
    <thead><tr><th>Model</th><th>$/1M in / out</th><th>Est. LLM</th><th>Est. 2× out</th><th>Actual</th></tr></thead>
    <tbody>${costRows}</tbody>`;

  const scoreRows = (data.models || []).map((m) => {
    if (m.status !== "complete") {
      return `<tr><td>${m.display}</td><td class="pending" colspan="6">${m.status}</td></tr>`;
    }
    return `<tr>
      <td>${m.display}</td>
      <td class="num">${m.n_pass}/${m.n_trials}</td>
      <td class="num">${pct(m.mean_reward)}</td>
      <td class="num">${m.n_errors}</td>
      <td class="num">${money(m.cost_usd)}</td>
      <td class="num">${m.total_runtime_sec ? Math.round(m.total_runtime_sec / 60) + " min" : "—"}</td>
      <td class="num">${(m.n_input_tokens || 0).toLocaleString()} / ${(m.n_output_tokens || 0).toLocaleString()}</td>
    </tr>`;
  }).join("");
  document.getElementById("score-table").innerHTML = `
    <thead><tr><th>Model</th><th>Pass</th><th>Mean</th><th>Errors</th><th>Cost</th><th>Runtime</th><th>Tokens in / out</th></tr></thead>
    <tbody>${scoreRows}</tbody>`;

  const levelRows = (data.models || []).map((m) => {
    const lvl = m.by_level || {};
    const cell = (k) => {
      const row = lvl[k];
      if (!row) return "—";
      return `${row.n_pass}/${row.n}`;
    };
    return `<tr>
      <td>${m.display}</td>
      <td class="num">${m.status === "complete" ? cell("L1") : "—"}</td>
      <td class="num">${m.status === "complete" ? cell("L2") : "—"}</td>
      <td class="num">${m.status === "complete" ? cell("L3") : "—"}</td>
    </tr>`;
  }).join("");
  document.getElementById("level-table").innerHTML = `
    <thead><tr><th>Model</th><th>L1 (5)</th><th>L2 (25)</th><th>L3 (20)</th></tr></thead>
    <tbody>${levelRows}</tbody>`;

  const models = data.models || [];
  const head = ["Task", "Lv", "Topic"].concat(models.map((m) => m.display));
  const body = (data.tasks || []).map((task) => {
    const cells = models.map((m) => {
      const v = (task.results || {})[m.id];
      if (v === 1) return `<td class="pass">pass</td>`;
      if (v === 0) return `<td class="fail">fail</td>`;
      return `<td class="pending">—</td>`;
    }).join("");
    return `<tr>
      <td class="task">${task.id}</td>
      <td>${task.level}</td>
      <td class="topic">${task.topic}</td>
      ${cells}
    </tr>`;
  }).join("");
  document.getElementById("matrix-table").innerHTML = `
    <thead><tr>${head.map((h) => `<th>${h}</th>`).join("")}</tr></thead>
    <tbody>${body}</tbody>`;
})();
