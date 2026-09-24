# Fixture + prompt definitions for the blind independent run.
# Each case: prompt (what a user would type), tools mode, files {path: content}.
# Fixtures intentionally contain NO comments that reveal the expected finding.

RO = "Skill Read Glob Grep"
FIX = "Skill Read Glob Grep Edit Write"
EXEC = "Skill Read Glob Grep Edit Write Bash"
WEB = "Skill Read Glob Grep WebSearch WebFetch"

CASES = {}

def case(cid, prompt, tools, files):
    CASES[cid] = dict(prompt=prompt, tools=tools, files=files)

# ---------------------------------------------------------------- Trigger
case("T1", "Something feels off about this dashboard spacing and hierarchy. Fix it.", FIX, {
"src/Dashboard.tsx": '''import "./dashboard.css";

type Kpi = { label: string; value: string; delta: string };

export function Dashboard({ kpis, alerts }: { kpis: Kpi[]; alerts: string[] }) {
  return (
    <div className="page">
      <div className="topbar">
        <span className="title">Fleet Maintenance</span>
        <button className="btn">Export</button>
        <button className="btn">Settings</button>
        <button className="btn">New work order</button>
      </div>
      <div className="kpis">
        {kpis.map((k) => (
          <div className="kpi" key={k.label}>
            <div className="kpi-label">{k.label}</div>
            <div className="kpi-value">{k.value}</div>
            <div className="kpi-delta">{k.delta}</div>
          </div>
        ))}
      </div>
      <div className="section">
        <div className="section-title">Overdue inspections</div>
        <ul className="alerts">
          {alerts.map((a) => <li key={a}>{a}</li>)}
        </ul>
      </div>
      <div className="section">
        <div className="section-title">Recent activity</div>
        <p className="muted">Truck 14 oil change logged by M. Ortiz</p>
      </div>
    </div>
  );
}
''',
"src/dashboard.css": '''.page { padding: 13px 22px 7px 30px; font-family: Inter, sans-serif; }
.topbar { display: flex; gap: 5px; align-items: center; margin-bottom: 9px; }
.title { font-size: 15px; font-weight: 600; }
.btn { padding: 11px 17px; font-size: 15px; font-weight: 600; border-radius: 6px; }
.kpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 27px; margin-bottom: 11px; }
.kpi { padding: 19px 12px; border: 1px solid #e5e5e5; border-radius: 14px; }
.kpi-label { font-size: 15px; font-weight: 600; }
.kpi-value { font-size: 16px; font-weight: 600; }
.kpi-delta { font-size: 15px; font-weight: 600; color: #888; }
.section { margin-top: 41px; padding: 6px; }
.section-title { font-size: 15px; font-weight: 600; margin-bottom: 3px; }
.alerts li { margin: 14px 0; }
.muted { color: #aaa; font-size: 15px; }
''',
"src/tokens.css": ''':root {
  --space-1: 4px; --space-2: 8px; --space-3: 12px; --space-4: 16px; --space-6: 24px; --space-8: 32px;
  --text-sm: 13px; --text-md: 15px; --text-lg: 20px; --text-xl: 28px;
  --radius-sm: 6px; --radius-md: 10px;
  --color-muted: #5f6368; --color-danger: #b3261e;
}
''',
})

case("T2", "Optimize this Postgres query.", FIX, {
"sql/monthly_revenue.sql": '''SELECT c.id, c.name,
       (SELECT SUM(o.total) FROM orders o WHERE o.customer_id = c.id
          AND date_trunc('month', o.created_at) = date_trunc('month', now())) AS month_total
FROM customers c
WHERE lower(c.email) LIKE '%@acme.com'
ORDER BY month_total DESC NULLS LAST;
''',
"sql/schema.sql": '''CREATE TABLE customers (id bigserial PRIMARY KEY, name text, email text);
CREATE TABLE orders (id bigserial PRIMARY KEY, customer_id bigint REFERENCES customers(id), total numeric(12,2), created_at timestamptz);
''',
})

case("T3", "My modal works with the mouse but keyboard users get stuck.", FIX, {
"src/ConfirmModal.tsx": '''import { useState } from "react";
import "./modal.css";

export function ArchiveProject({ onArchive }: { onArchive: () => void }) {
  const [open, setOpen] = useState(false);
  return (
    <>
      <button onClick={() => setOpen(true)}>Archive project</button>
      {open && (
        <div className="overlay" onClick={() => setOpen(false)}>
          <div className="modal" onClick={(e) => e.stopPropagation()}>
            <div className="modal-title">Archive this project?</div>
            <p>Members will lose edit access. You can restore it within 30 days.</p>
            <div className="actions">
              <div className="btn" onClick={() => setOpen(false)}>Cancel</div>
              <div className="btn primary" onClick={() => { onArchive(); setOpen(false); }}>Archive</div>
            </div>
            <span className="close" onClick={() => setOpen(false)}>✕</span>
          </div>
        </div>
      )}
    </>
  );
}
''',
"src/modal.css": '''.overlay { position: fixed; inset: 0; background: rgba(0,0,0,.45); display: grid; place-items: center; }
.modal { background: #fff; padding: 24px; border-radius: 8px; width: 420px; position: relative; }
.modal-title { font-size: 18px; font-weight: 600; }
.btn { display: inline-block; padding: 8px 14px; cursor: pointer; }
.btn:focus, .close:focus { outline: none; }
.primary { background: #0b57d0; color: #fff; }
.close { position: absolute; top: 12px; right: 12px; cursor: pointer; }
''',
})

# ---------------------------------------------------------------- Review
case("R1", "Review this landing page before we launch. The product is Samplyr, sample-tracking software for small biotech labs.", RO, {
"index.html": '''<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Samplyr</title><link rel="stylesheet" href="style.css"></head>
<body>
<nav class="nav"><span class="logo">Samplyr</span><a href="#features">Features</a><a href="#pricing">Pricing</a><a href="#contact">Contact</a><a class="pill" href="/signup">Get started →</a></nav>
<header class="hero">
  <h1 class="gradient-text">Transform Your Workflow with AI-Powered Innovation</h1>
  <p>Unlock the power of next-generation intelligence to supercharge your team and scale seamlessly.</p>
  <a class="pill big" href="/signup">Start your journey →</a>
</header>
<section id="features" class="card glass">
  <div class="trio">
    <div class="card glass"><span class="icon">⚡</span><h3>Lightning Fast</h3><p>Blazing performance that scales.</p></div>
    <div class="card glass"><span class="icon">🔒</span><h3>Secure by Design</h3><p>Enterprise-grade security you can trust.</p></div>
    <div class="card glass"><span class="icon">✨</span><h3>AI-Powered</h3><p>Smart insights that drive results.</p></div>
  </div>
</section>
<section class="card glass"><h2>Trusted by 10,000+ teams worldwide</h2><p>"Samplyr changed everything." — Happy Customer</p></section>
<section id="contact" class="card glass">
  <h2>Stay in the loop</h2>
  <form><input type="email" placeholder="Your email"><div class="pill" onclick="subscribe()">Subscribe</div></form>
</section>
<script>function subscribe(){ alert('Subscribed!'); }</script>
</body></html>
''',
"style.css": '''body { margin: 0; font-family: "Inter", sans-serif; background: linear-gradient(135deg, #6d28d9, #2563eb); color: #fff; }
.nav { display: flex; gap: 32px; padding: 20px 64px; align-items: center; }
.nav a { color: rgba(255,255,255,.7); }
.hero { text-align: center; padding: 160px 64px; }
.gradient-text { background: linear-gradient(90deg,#c4b5fd,#93c5fd); -webkit-background-clip: text; color: transparent; font-size: 72px; }
.card { border-radius: 32px; padding: 48px; margin: 32px 64px; }
.glass { background: rgba(255,255,255,.08); backdrop-filter: blur(16px); border: 1px solid rgba(255,255,255,.18); box-shadow: 0 0 40px rgba(139,92,246,.4); }
.trio { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.trio .card { margin: 0; }
.pill { display: inline-block; border-radius: 999px; padding: 12px 28px; background: linear-gradient(90deg,#8b5cf6,#3b82f6); color: #fff; cursor: pointer; }
.big { padding: 18px 40px; font-size: 20px; }
p { color: rgba(255,255,255,.6); }
input { border-radius: 999px; padding: 12px 20px; border: 0; }
''',
})

case("R2", "Review this signup flow UI and tell me what to fix first.", RO, {
"src/Signup.tsx": '''import { useState } from "react";
import "./signup.css";

export function Signup() {
  const [email, setEmail] = useState("");
  const [err, setErr] = useState("");
  const [terms, setTerms] = useState(false);
  return (
    <div className="card">
      <div className="h">Create your account</div>
      <label>Email</label>
      <input value={email} onChange={(e) => setEmail(e.target.value)} />
      {err && <div className="error">{err}</div>}
      <div className="link" onClick={() => setTerms(true)}>View terms</div>
      <div className="cta" onClick={() => setErr(email.includes("@") ? "" : "Enter a valid email")}>Sign up</div>
      {terms && (
        <div className="modal-backdrop">
          <div className="modal">
            <div className="h">Terms of service</div>
            <div className="terms-body">...long terms text...</div>
            <div className="cta" onClick={() => setTerms(false)}>Close</div>
          </div>
        </div>
      )}
    </div>
  );
}
''',
"src/signup.css": '''.card { padding: 28px; border-radius: 18px; box-shadow: 0 6px 30px rgba(0,0,0,.08); max-width: 380px; }
.h { font-size: 22px; font-weight: 700; margin-bottom: 14px; }
input { width: 100%; padding: 10px; border-radius: 10px; border: 1px solid #ddd; }
input:focus, .cta:focus, .link:focus { outline: none; }
.error { color: #e11d48; font-size: 12px; }
.link { color: #2563eb; cursor: pointer; margin: 12px 0; }
.cta { background: #111; color: #fff; text-align: center; padding: 12px; border-radius: 12px; cursor: pointer; }
.modal-backdrop { position: fixed; inset: 0; background: rgba(0,0,0,.5); display: grid; place-items: center; }
.modal { background: #fff; padding: 24px; border-radius: 22px; max-width: 520px; }
.terms-body { max-height: 300px; overflow: auto; }
''',
})

case("R3", "Review the responsive behavior of this claims screen. Our reviewers use it on phones as well as desktops.", EXEC, {
"claims.html": '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Claims queue</title>
<style>
body { margin: 0; font: 16px system-ui; display: flex; }
aside { width: 260px; flex: none; padding: 20px; border-right: 1px solid #ddd; min-height: 100vh; }
main { padding: 20px; padding-bottom: 80px; }
table { border-collapse: collapse; width: 720px; }
th, td { padding: 10px 14px; border: 1px solid #ddd; white-space: nowrap; text-align: left; }
.footer { position: fixed; bottom: 0; left: 0; right: 0; height: 64px; background: #fff; border-top: 1px solid #ddd; display: flex; justify-content: flex-end; align-items: center; padding: 0 20px; }
textarea { width: 100%; min-height: 140px; }
.submit { padding: 12px 20px; }
</style></head>
<body>
<aside><nav><a href="/queue">Queue</a><br><a href="/reports">Reports</a><br><a href="/settings">Settings</a></nav></aside>
<main>
  <h1>Claims queue</h1>
  <table>
    <thead><tr><th>Patient</th><th>Status</th><th>Payer</th><th>Last updated</th></tr></thead>
    <tbody>
      <tr><td>Alexandria Montgomery-Whitfield</td><td>Needs clinical review</td><td>Blue Horizon Health Plan</td><td>2026-09-23 16:42</td></tr>
      <tr><td>Omar Al-Harbi</td><td>Pending documents</td><td>National Mutual</td><td>2026-09-24 08:10</td></tr>
    </tbody>
  </table>
  <form>
    <label for="note">Reviewer note</label>
    <textarea id="note"></textarea>
    <button class="submit" type="submit">Submit review</button>
  </form>
</main>
<div class="footer"><span>2 claims selected</span><button>Approve selected</button></div>
</body></html>
''',
})

case("R4", "Review this orders page component.", RO, {
"src/OrdersPage.tsx": '''import { useEffect, useState } from "react";
import { api } from "./api";

type Order = { id: string; customer: string; total: number; status: string };

export function OrdersPage() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [note, setNote] = useState("");

  useEffect(() => {
    api.get<Order[]>("/orders").then(setOrders);
  }, []);

  async function submitRefund(id: string) {
    await api.post(`/orders/${id}/refund`, { note });
    setOrders((o) => o.map((x) => (x.id === id ? { ...x, status: "refunded" } : x)));
  }

  return (
    <main>
      <h1>Orders</h1>
      <table>
        <thead><tr><th>Order</th><th>Customer</th><th>Total</th><th>Status</th><th></th></tr></thead>
        <tbody>
          {orders.map((o) => (
            <tr key={o.id}>
              <td>{o.id}</td><td>{o.customer}</td><td>{o.total}</td><td>{o.status}</td>
              <td><button onClick={() => submitRefund(o.id)}>Refund</button></td>
            </tr>
          ))}
        </tbody>
      </table>
      <label htmlFor="note">Refund note</label>
      <input id="note" value={note} onChange={(e) => setNote(e.target.value)} />
    </main>
  );
}
''',
"src/api.ts": '''export const api = {
  async get<T>(url: string): Promise<T> { const r = await fetch(url); if (!r.ok) throw new Error(String(r.status)); return r.json(); },
  async post(url: string, body: unknown) { const r = await fetch(url, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) }); if (!r.ok) throw new Error(String(r.status)); return r.json(); },
};
''',
})

case("R5", "Users say our signup form is frustrating. Review it.", RO, {
"src/SignupForm.tsx": '''import { useState } from "react";

const initial = { name: "", email: "", password: "" };

export function SignupForm() {
  const [form, setForm] = useState(initial);
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [serverError, setServerError] = useState("");

  function validate(f: typeof initial) {
    const e: Record<string, string> = {};
    if (!f.name) e.name = "Required";
    if (!/^\\S+@\\S+$/.test(f.email)) e.email = "Invalid email";
    if (!/^(?=.*[A-Z])(?=.*\\d)(?=.*[^\\w]).{12,}$/.test(f.password))
      e.password = "Password must be 12+ characters with an uppercase letter, a number and a symbol";
    return e;
  }

  function onChange(field: keyof typeof initial, value: string) {
    const next = { ...form, [field]: value };
    setForm(next);
    setErrors(validate(next));
  }

  async function onSubmit(ev: React.FormEvent) {
    ev.preventDefault();
    const e = validate(form);
    setErrors(e);
    if (Object.keys(e).length) return;
    const res = await fetch("/api/signup", { method: "POST", body: JSON.stringify(form) });
    if (!res.ok) {
      setServerError("Something went wrong");
      setForm(initial);
    }
  }

  return (
    <form onSubmit={onSubmit}>
      <input placeholder="Full name" value={form.name} onChange={(e) => onChange("name", e.target.value)} />
      {errors.name && <span className="err">{errors.name}</span>}
      <input placeholder="Email" value={form.email} onChange={(e) => onChange("email", e.target.value)} />
      {errors.email && <span className="err">{errors.email}</span>}
      <input placeholder="Password" type="password" value={form.password} onChange={(e) => onChange("password", e.target.value)} />
      {errors.password && <span className="err">{errors.password}</span>}
      {serverError && <p className="err">{serverError}</p>}
      <button type="submit">Create account</button>
    </form>
  );
}
''',
})

case("R6", "Review this admin users table.", RO, {
"src/UsersTable.tsx": '''import { useState } from "react";
import { useUsers, deleteUsers } from "./data";
import "./table.css";

export function UsersTable() {
  const [sort, setSort] = useState<{ key: string; dir: "asc" | "desc" }>({ key: "name", dir: "asc" });
  const [page, setPage] = useState(1);
  const [filters, setFilters] = useState({ role: "", status: "" });
  const [showFilters, setShowFilters] = useState(false);
  const [selected, setSelected] = useState<string[]>([]);
  const { rows, total } = useUsers({ sort, page, filters, pageSize: 25 });

  const toggleSort = (key: string) => setSort((s) => ({ key, dir: s.key === key && s.dir === "asc" ? "desc" : "asc" }));

  return (
    <div>
      <div className="toolbar">
        <button onClick={() => setShowFilters(!showFilters)}>Filters</button>
        <button className="danger" onClick={() => deleteUsers(selected)}>Delete</button>
      </div>
      {showFilters && (
        <div className="filters">
          <select value={filters.role} onChange={(e) => setFilters({ ...filters, role: e.target.value })}>
            <option value="">Any role</option><option>admin</option><option>editor</option><option>viewer</option>
          </select>
          <select value={filters.status} onChange={(e) => setFilters({ ...filters, status: e.target.value })}>
            <option value="">Any status</option><option>active</option><option>suspended</option>
          </select>
        </div>
      )}
      <div className="grid header">
        <div><input type="checkbox" onChange={(e) => setSelected(e.target.checked ? rows.map((r) => r.id) : [])} /> Select all</div>
        <div onClick={() => toggleSort("name")}>Name</div>
        <div onClick={() => toggleSort("email")}>Email</div>
        <div onClick={() => toggleSort("role")}>Role</div>
        <div onClick={() => toggleSort("lastActive")}>Last active</div>
      </div>
      {rows.map((r) => (
        <div className="grid" key={r.id}>
          <div><input type="checkbox" checked={selected.includes(r.id)} onChange={() => setSelected((s) => s.includes(r.id) ? s.filter((x) => x !== r.id) : [...s, r.id])} /></div>
          <div>{r.name}</div><div>{r.email}</div><div>{r.role}</div><div>{r.lastActive}</div>
        </div>
      ))}
      <div className="pager">
        <button onClick={() => setPage(page - 1)}>Prev</button>
        <span>{page}</span>
        <button onClick={() => setPage(page + 1)}>Next</button>
      </div>
      <p>{total} users</p>
    </div>
  );
}
''',
"src/table.css": '''.grid { display: grid; grid-template-columns: 140px 220px 280px 120px 160px; }
.grid.header div { font-weight: 600; cursor: pointer; }
.danger { background: #c62828; color: #fff; }
''',
})

case("R7", "Review our new hero section.", RO, {
"docs/brand-guidelines.md": '''# Lumina Pay brand guidelines (v3, approved by Brand Council 2026-03)

- Primary brand surface: the "Lumina sweep" gradient, #5B21B6 -> #7C3AED -> #A78BFA, left to right. It is mandatory on the homepage hero.
- All primary and secondary buttons are fully rounded pills (radius 999px). This is part of our trademarked visual identity.
- Typeface: "Lumina Sans" (licensed), fallback system-ui.
- Text on the sweep must meet WCAG 2.2 AA contrast.
''',
"src/Hero.tsx": '''import "./hero.css";

export function Hero() {
  return (
    <section className="hero">
      <h1>Get paid in 190 countries, settle in your local currency</h1>
      <p className="sub">Lumina Pay handles invoicing, FX and payouts for freelancers. Fees from 0.9% per transfer.</p>
      <div className="ctas">
        <a className="pill primary" href="/signup">Open a free account</a>
        <a className="pill secondary" href="/pricing">See fees</a>
      </div>
    </section>
  );
}
''',
"src/hero.css": '''.hero { background: linear-gradient(90deg, #5B21B6, #7C3AED, #A78BFA); padding: 96px 48px; color: #fff; font-family: "Lumina Sans", system-ui; }
.hero h1 { font-size: 56px; max-width: 18ch; }
.sub { max-width: 52ch; color: #fff; }
.ctas { display: flex; gap: 12px; justify-content: flex-end; }
.pill { border-radius: 999px; padding: 14px 28px; text-decoration: none; }
.primary { background: #fff; color: #5B21B6; }
.secondary { background: rgba(255,255,255,.25); color: #fff; }
''',
})

case("R8", "Review our UI code for consistency issues.", RO, {
"components/ui/button.tsx": '''import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        ghost: "hover:bg-accent hover:text-accent-foreground",
      },
      size: { default: "h-10 px-4 py-2", sm: "h-9 rounded-md px-3", lg: "h-11 rounded-md px-8" },
    },
    defaultVariants: { variant: "default", size: "default" },
  }
);

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement>, VariantProps<typeof buttonVariants> {}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(({ className, variant, size, ...props }, ref) => (
  <button className={cn(buttonVariants({ variant, size, className }))} ref={ref} {...props} />
));
''',
"app/projects/page.tsx": '''import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";

export default function Projects() {
  return (
    <div className="p-6">
      <div className="flex justify-between">
        <h1 className="text-2xl font-semibold">Projects</h1>
        <button className="bg-blue-600 text-white rounded-xl px-5 py-2.5 hover:bg-blue-700">New project</button>
      </div>
      <Card className="mt-6 rounded-2xl">
        <CardHeader><CardTitle>Active</CardTitle></CardHeader>
        <CardContent><Button>Open</Button></CardContent>
      </Card>
    </div>
  );
}
''',
"app/settings/page.tsx": '''import { Button } from "@/components/ui/button";

export default function Settings() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold">Settings</h1>
      <section className="mt-4 border rounded-lg p-5">
        <h2 className="font-medium">Danger zone</h2>
        <button className="bg-red-500 text-white rounded-full px-4 py-2">Delete workspace</button>
        <Button variant="outline" className="rounded-full">Cancel</Button>
      </section>
    </div>
  );
}
''',
"app/billing/page.tsx": '''export default function Billing() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-semibold">Billing</h1>
      <div className="mt-6 rounded-3xl border p-6 shadow-lg">
        <p className="text-sm text-gray-500">Current plan: Team</p>
        <button className="mt-4 bg-[#2563eb] text-white rounded-lg px-4 py-2 focus:outline-none">Upgrade</button>
      </div>
    </div>
  );
}
''',
"tailwind.config.ts": '''export default {
  theme: { extend: { borderRadius: { lg: "var(--radius)", md: "calc(var(--radius) - 2px)", sm: "calc(var(--radius) - 4px)" },
    colors: { primary: { DEFAULT: "hsl(var(--primary))", foreground: "hsl(var(--primary-foreground))" }, destructive: { DEFAULT: "hsl(var(--destructive))", foreground: "hsl(var(--destructive-foreground))" } } } },
};
''',
"app/globals.css": ''':root { --radius: 0.5rem; --primary: 222.2 47.4% 11.2%; --primary-foreground: 210 40% 98%; --destructive: 0 84.2% 60.2%; --destructive-foreground: 210 40% 98%; }
''',
})

case("R9", "This is the Arabic version of our order details screen. Review it.", EXEC, {
"src/OrderDetails.tsx": '''import { ChevronRight, ArrowLeft } from "lucide-react";

type Order = { id: string; customerName: string; placedAt: string; total: number; items: { name: string; qty: number }[] };

export function OrderDetails({ order, t }: { order: Order; t: (k: string) => string }) {
  return (
    <div dir="rtl" lang="ar" className="p-4">
      <a href="/orders" className="flex items-center text-left">
        <ArrowLeft className="mr-2" /> {t("back_to_orders")}
      </a>
      <h1 className="text-left text-2xl">{t("order")} #{order.id}</h1>
      <p className="ml-4">{t("customer")}: {order.customerName}</p>
      <p className="ml-4">{t("placed_on")}: {new Date(order.placedAt).toLocaleDateString("en-US")}</p>
      <p className="ml-4">{t("total")}: ${order.total.toFixed(2)}</p>
      <ul>
        {order.items.map((i) => (
          <li key={i.name} className="flex justify-between pl-3 border-l-4">
            <span>{i.name}</span>
            <span>{i.qty} {t("items")}</span>
            <ChevronRight />
          </li>
        ))}
      </ul>
      <button className="w-32 whitespace-nowrap overflow-hidden rounded bg-blue-600 text-white px-3 py-2">{t("request_return")}</button>
    </div>
  );
}
''',
"locales/ar.json": '''{
  "back_to_orders": "العودة إلى الطلبات",
  "order": "الطلب",
  "customer": "العميل",
  "placed_on": "تاريخ الطلب",
  "total": "الإجمالي",
  "items": "قطع",
  "request_return": "طلب إرجاع المنتجات واسترداد المبلغ"
}
''',
})

case("R10", "Review this revenue chart component.", RO, {
"src/RevenueChart.tsx": '''import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

type Point = { month: string; actual: number; target: number };

export function RevenueChart({ data }: { data: Point[] }) {
  return (
    <div className="chart-card">
      <h3>Revenue</h3>
      <ResponsiveContainer width="100%" height={280}>
        <LineChart data={data}>
          <XAxis dataKey="month" tick={false} />
          <YAxis tick={false} domain={[80000, "auto"]} />
          <Tooltip />
          <Line type="monotone" dataKey="actual" stroke="#16a34a" dot={false} />
          <Line type="monotone" dataKey="target" stroke="#dc2626" dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
''',
})

# ---------------------------------------------------------------- Generation
GEN_README = {"README.md": "Static site project. Plain HTML/CSS/JS only, no build step, no external dependencies. Put deliverables in this folder.\n"}
case("G1", "Build a professional analytics dashboard.", EXEC, dict(GEN_README))
case("G2", "Build my portfolio for a healthcare informatics professional with AI side projects.", EXEC, dict(GEN_README))
case("G3", "Create a mobile insurance authorization form.", EXEC, dict(GEN_README))

# ---------------------------------------------------------------- False positive
case("F1", "Review this work-orders screen.", RO, {
"src/WorkOrders.tsx": '''import "./workorders.css";

type WO = { id: string; asset: string; issue: string; priority: "P1" | "P2" | "P3"; assignee?: string; due: string };

export function WorkOrders({ items, onAssign, onClose, loading, error, retry }: {
  items: WO[]; onAssign: (id: string) => void; onClose: (id: string) => void; loading: boolean; error?: string; retry: () => void;
}) {
  if (loading) return <p role="status">Loading work orders…</p>;
  if (error) return <div role="alert"><p>Couldn't load work orders: {error}</p><button onClick={retry}>Try again</button></div>;
  if (!items.length) return <p>No open work orders. New requests from technicians will appear here.</p>;
  return (
    <main>
      <h1>Open work orders <span className="count">({items.length})</span></h1>
      <ul className="wo-list">
        {items.map((wo) => (
          <li key={wo.id} className="wo-card">
            <article aria-labelledby={`wo-${wo.id}`}>
              <h2 id={`wo-${wo.id}`}>{wo.asset}</h2>
              <p>{wo.issue}</p>
              <dl>
                <dt>Priority</dt><dd className={`prio prio-${wo.priority}`}>{wo.priority}</dd>
                <dt>Assignee</dt><dd>{wo.assignee ?? "Unassigned"}</dd>
                <dt>Due</dt><dd><time dateTime={wo.due}>{new Date(wo.due).toLocaleDateString()}</time></dd>
              </dl>
              <div className="actions">
                <button onClick={() => onAssign(wo.id)}>Assign {wo.asset}</button>
                <button onClick={() => onClose(wo.id)}>Close work order</button>
              </div>
            </article>
          </li>
        ))}
      </ul>
    </main>
  );
}
''',
"src/workorders.css": ''':root { --space-2: 8px; --space-3: 12px; --space-4: 16px; --radius: 6px; --border: #d0d4d9; --text: #1b1f24; --muted: #57606a; }
.wo-list { list-style: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr)); gap: var(--space-4); }
.wo-card { border: 1px solid var(--border); border-radius: var(--radius); padding: var(--space-4); color: var(--text); }
.wo-card h2 { font-size: 1.05rem; margin: 0 0 var(--space-2); }
dl { display: grid; grid-template-columns: auto 1fr; gap: var(--space-2) var(--space-3); color: var(--muted); }
.actions { display: flex; flex-wrap: wrap; gap: var(--space-2); margin-top: var(--space-3); }
.actions button { min-height: 44px; padding: 0 var(--space-4); }
.prio-P1::before { content: "▲ "; }
.count { color: var(--muted); font-weight: 400; }
button:focus-visible { outline: 3px solid #0b57d0; outline-offset: 2px; }
''',
})

case("F2", "Review this priority queue component.", RO, {
"src/PriorityQueue.tsx": '''import { useLayoutEffect, useRef } from "react";
import "./queue.css";

type Item = { id: string; title: string; score: number };

export function PriorityQueue({ items, onBump }: { items: Item[]; onBump: (id: string) => void }) {
  const positions = useRef(new Map<string, number>());
  const listRef = useRef<HTMLOListElement>(null);

  useLayoutEffect(() => {
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const nodes = listRef.current?.querySelectorAll<HTMLElement>("[data-id]") ?? [];
    nodes.forEach((el) => {
      const id = el.dataset.id!;
      const top = el.getBoundingClientRect().top;
      const prev = positions.current.get(id);
      if (!reduce && prev !== undefined && prev !== top) {
        el.animate([{ transform: `translateY(${prev - top}px)` }, { transform: "none" }], { duration: 180, easing: "ease-out" });
      }
      positions.current.set(id, top);
    });
  }, [items]);

  return (
    <section aria-labelledby="pq-h">
      <h2 id="pq-h">Triage queue</h2>
      <p id="pq-status" role="status" className="sr-only">{items[0] ? `${items[0].title} is now first` : ""}</p>
      <ol ref={listRef} className="pq">
        {items.map((it, i) => (
          <li key={it.id} data-id={it.id}>
            <span className="rank">{i + 1}</span>
            <span className="title">{it.title}</span>
            <span className="score">Score {it.score}</span>
            <button onClick={() => onBump(it.id)}>Move up</button>
          </li>
        ))}
      </ol>
    </section>
  );
}
''',
"src/queue.css": '''.pq { list-style: none; padding: 0; margin: 0; }
.pq li { display: grid; grid-template-columns: 2ch 1fr auto auto; gap: 12px; align-items: center; padding: 10px 0; border-bottom: 1px solid #ddd; }
.pq button { min-height: 40px; }
.pq button:focus-visible { outline: 2px solid #0b57d0; outline-offset: 2px; }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
@media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto !important; } }
''',
})

case("F3", "Review the accessibility of this notification settings panel and fix anything that needs fixing.", FIX, {
"src/NotificationSettings.tsx": '''import { useState } from "react";

export function NotificationSettings({ onSave }: { onSave: (s: unknown) => Promise<void> }) {
  const [digest, setDigest] = useState("daily");
  const [email, setEmail] = useState(true);
  const [sms, setSms] = useState(false);
  const [status, setStatus] = useState("");
  const [saving, setSaving] = useState(false);

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    setSaving(true);
    try { await onSave({ digest, email, sms }); setStatus("Notification settings saved."); }
    catch { setStatus("Couldn't save settings. Your changes are still here, try again."); }
    finally { setSaving(false); }
  }

  return (
    <form onSubmit={submit}>
      <h2>Notifications</h2>
      <fieldset>
        <legend>Channels</legend>
        <label><input type="checkbox" checked={email} onChange={(e) => setEmail(e.target.checked)} /> Email</label>
        <label><input type="checkbox" checked={sms} onChange={(e) => setSms(e.target.checked)} /> SMS</label>
      </fieldset>
      <label htmlFor="digest">Digest frequency</label>
      <select id="digest" value={digest} onChange={(e) => setDigest(e.target.value)}>
        <option value="off">Off</option>
        <option value="daily">Daily</option>
        <option value="weekly">Weekly</option>
      </select>
      <details>
        <summary>What counts as a notification?</summary>
        <p>Mentions, assignments, and status changes on items you follow.</p>
      </details>
      <button type="submit" disabled={saving}>{saving ? "Saving…" : "Save settings"}</button>
      <p role="status">{status}</p>
    </form>
  );
}
''',
"src/settings.css": '''form { max-width: 480px; display: grid; gap: 12px; }
fieldset { border: 1px solid #c4c7cc; padding: 12px; }
label { display: block; }
button { min-height: 44px; }
:focus-visible { outline: 2px solid #0b57d0; outline-offset: 2px; }
''',
})

# ---------------------------------------------------------------- Security
case("S1", "Do a security review of this admin projects UI.", RO, {
"src/ProjectRow.tsx": '''import { api } from "./api";
import { useCurrentUser } from "./auth";

export function ProjectRow({ project }: { project: { id: string; name: string; ownerId: string } }) {
  const user = useCurrentUser();
  return (
    <tr>
      <td>{project.name}</td>
      <td>
        {user.role === "admin" && (
          <button onClick={() => api.del(`/api/projects/${project.id}`)}>Delete project</button>
        )}
      </td>
    </tr>
  );
}
''',
"src/api.ts": '''const base = import.meta.env.VITE_API_URL;
export const api = {
  del: (path: string) => fetch(base + path, { method: "DELETE", credentials: "include" }),
  get: (path: string) => fetch(base + path, { credentials: "include" }).then((r) => r.json()),
};
''',
"src/auth.ts": '''import { useContext } from "react";
import { UserContext } from "./UserContext";
export function useCurrentUser() { return useContext(UserContext); }
''',
})

case("S2", "Review this comments component.", RO, {
"src/Comment.tsx": '''import { marked } from "marked";

type Comment = { id: string; author: string; body: string; createdAt: string };

export function CommentItem({ comment }: { comment: Comment }) {
  const html = marked.parse(comment.body) as string;
  return (
    <article className="comment">
      <header><strong>{comment.author}</strong> <time dateTime={comment.createdAt}>{comment.createdAt}</time></header>
      <div className="comment-body" dangerouslySetInnerHTML={{ __html: html }} />
    </article>
  );
}
''',
"src/CommentForm.tsx": '''import { useState } from "react";
export function CommentForm({ onPost }: { onPost: (body: string) => void }) {
  const [body, setBody] = useState("");
  return (
    <form onSubmit={(e) => { e.preventDefault(); onPost(body); setBody(""); }}>
      <label htmlFor="c">Add a comment (Markdown supported)</label>
      <textarea id="c" value={body} onChange={(e) => setBody(e.target.value)} />
      <button type="submit">Post</button>
    </form>
  );
}
''',
})

case("S3", "Review the auth/session handling in our patient portal frontend.", RO, {
"src/session.ts": '''export async function login(email: string, password: string) {
  const res = await fetch("/api/login", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ email, password }) });
  const { accessToken, user } = await res.json();
  localStorage.setItem("accessToken", accessToken);
  localStorage.setItem("user", JSON.stringify(user));
}

export function authHeader() {
  return { Authorization: `Bearer ${localStorage.getItem("accessToken")}` };
}

export function logout() {
  window.location.href = "/login";
}
''',
"src/records.ts": '''import { authHeader } from "./session";

export async function loadRecords() {
  const cached = localStorage.getItem("records");
  if (cached) return JSON.parse(cached);
  const res = await fetch("/api/records", { headers: authHeader() });
  const records = await res.json();
  localStorage.setItem("records", JSON.stringify(records));
  return records;
}
''',
"src/types.ts": '''export type PatientRecord = { mrn: string; name: string; dob: string; diagnoses: string[]; medications: string[]; labResults: { test: string; value: string }[] };
''',
})

case("S4", "Review our login flow code.", RO, {
"src/Login.tsx": '''import { useState } from "react";

export function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    const res = await fetch("/api/session", { method: "POST", credentials: "include", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ email, password }) });
    if (!res.ok) { setError("Email or password is incorrect."); return; }
    const next = new URLSearchParams(window.location.search).get("next") || "/home";
    window.location.href = next;
  }

  return (
    <form onSubmit={submit}>
      <label htmlFor="email">Email</label>
      <input id="email" type="email" autoComplete="username" value={email} onChange={(e) => setEmail(e.target.value)} />
      <label htmlFor="pw">Password</label>
      <input id="pw" type="password" autoComplete="current-password" value={password} onChange={(e) => setPassword(e.target.value)} />
      {error && <p role="alert">{error}</p>}
      <button type="submit">Sign in</button>
    </form>
  );
}
''',
})

case("S5", "Review this document upload screen.", RO, {
"src/UploadReferral.tsx": '''import { useState } from "react";

export function UploadReferral() {
  const [file, setFile] = useState<File | null>(null);
  const [msg, setMsg] = useState("");

  function pick(e: React.ChangeEvent<HTMLInputElement>) {
    const f = e.target.files?.[0];
    if (!f) return;
    if (f.type !== "application/pdf" || !f.name.toLowerCase().endsWith(".pdf")) { setMsg("Only PDF files are allowed."); return; }
    setFile(f);
    setMsg("✓ Your file has been securely validated and is safe to upload.");
  }

  async function upload() {
    if (!file) return;
    const body = new FormData(); body.append("file", file);
    await fetch("/api/referrals/upload", { method: "POST", body, credentials: "include" });
    setMsg("Uploaded.");
  }

  return (
    <div>
      <label htmlFor="ref">Referral letter (PDF)</label>
      <input id="ref" type="file" accept=".pdf,application/pdf" onChange={pick} />
      <p>{msg}</p>
      <button onClick={upload} disabled={!file}>Upload</button>
    </div>
  );
}
''',
})

case("S6", "Review this patient intake form.", RO, {
"src/IntakeForm.tsx": '''import { useState } from "react";
import { analytics } from "./analytics";

const empty = { fullName: "", dob: "", phone: "", nationalId: "", insuranceNumber: "", symptoms: "", currentMedications: "", pregnant: "" };

export function IntakeForm({ onSubmit }: { onSubmit: (v: typeof empty) => Promise<void> }) {
  const [v, setV] = useState(empty);
  const set = (k: keyof typeof empty) => (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => setV({ ...v, [k]: e.target.value });

  async function submit(e: React.FormEvent) {
    e.preventDefault();
    analytics.track("intake_submitted", { ...v, ts: Date.now() });
    await onSubmit(v);
  }

  return (
    <form onSubmit={submit}>
      <label htmlFor="n">Full name</label><input id="n" value={v.fullName} onChange={set("fullName")} autoComplete="name" />
      <label htmlFor="d">Date of birth</label><input id="d" type="date" value={v.dob} onChange={set("dob")} autoComplete="bday" />
      <label htmlFor="p">Phone</label><input id="p" type="tel" value={v.phone} onChange={set("phone")} autoComplete="tel" />
      <label htmlFor="nid">National ID</label><input id="nid" value={v.nationalId} onChange={set("nationalId")} />
      <label htmlFor="ins">Insurance number</label><input id="ins" value={v.insuranceNumber} onChange={set("insuranceNumber")} />
      <label htmlFor="s">Symptoms</label><textarea id="s" value={v.symptoms} onChange={set("symptoms")} />
      <label htmlFor="m">Current medications</label><textarea id="m" value={v.currentMedications} onChange={set("currentMedications")} />
      <label htmlFor="pr">Pregnancy status</label><input id="pr" value={v.pregnant} onChange={set("pregnant")} />
      <button type="submit">Submit intake</button>
    </form>
  );
}
''',
"src/analytics.ts": '''export const analytics = {
  track(event: string, props: Record<string, unknown>) {
    navigator.sendBeacon("https://collect.example-analytics.io/v1/e", JSON.stringify({ event, props, url: location.href }));
  },
};
''',
})

case("S7", "Do a security review of this frontend.", RO, {
"package.json": '''{ "name": "team-notes", "private": true, "type": "module",
  "scripts": { "dev": "vite", "build": "vite build" },
  "dependencies": { "react": "^18.3.1", "react-dom": "^18.3.1" },
  "devDependencies": { "vite": "^5.4.0", "@vitejs/plugin-react": "^4.3.1", "typescript": "^5.5.0" } }
''',
"index.html": '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Team Notes</title></head><body><div id="root"></div><script type="module" src="/src/main.tsx"></script></body></html>
''',
"src/main.tsx": '''import { createRoot } from "react-dom/client";
import { App } from "./App";
createRoot(document.getElementById("root")!).render(<App />);
''',
"src/App.tsx": '''import { useEffect, useState } from "react";

type Note = { id: string; title: string; body: string };

export function App() {
  const [notes, setNotes] = useState<Note[]>([]);
  const [error, setError] = useState("");
  useEffect(() => {
    fetch("/api/notes", { credentials: "include" })
      .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
      .then(setNotes)
      .catch(() => setError("Couldn't load notes."));
  }, []);
  return (
    <main>
      <h1>Team notes</h1>
      {error && <p role="alert">{error}</p>}
      <ul>{notes.map((n) => <li key={n.id}><h2>{n.title}</h2><p>{n.body}</p></li>)}</ul>
    </main>
  );
}
''',
"vite.config.ts": '''import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig({ plugins: [react()] });
''',
})

case("S8", "Review our AI assistant panel.", RO, {
"src/AssistantPanel.tsx": '''import { useState } from "react";

type ModelReply = { html: string; action?: { type: "open_url" | "call_api"; url: string; method?: string; body?: unknown } };

export function AssistantPanel() {
  const [q, setQ] = useState("");
  const [reply, setReply] = useState<ModelReply | null>(null);

  async function ask() {
    const res = await fetch("/api/assistant", { method: "POST", credentials: "include", body: JSON.stringify({ q }) });
    const r: ModelReply = await res.json();
    setReply(r);
    if (r.action?.type === "open_url") window.location.href = r.action.url;
    if (r.action?.type === "call_api") await fetch(r.action.url, { method: r.action.method ?? "POST", credentials: "include", body: JSON.stringify(r.action.body) });
  }

  return (
    <aside>
      <label htmlFor="q">Ask the assistant</label>
      <textarea id="q" value={q} onChange={(e) => setQ(e.target.value)} />
      <button onClick={ask}>Ask</button>
      {reply && <div className="reply" dangerouslySetInnerHTML={{ __html: reply.html }} />}
    </aside>
  );
}
''',
"README.md": "The assistant can read the user's tickets and customer records (retrieved server-side) and suggest actions like refunds or account changes.\n",
})

case("S9", "Is our frontend's dependency setup secure?", RO, {
"package.json": '''{
  "name": "clinic-scheduler-web",
  "private": true,
  "scripts": { "dev": "next dev", "build": "next build", "start": "next start" },
  "dependencies": {
    "next": "14.2.15",
    "react": "18.3.1",
    "react-dom": "18.3.1",
    "date-fns": "^3.6.0",
    "zod": "^3.23.8",
    "@tanstack/react-query": "^5.59.0",
    "clsx": "^2.1.1"
  },
  "devDependencies": { "typescript": "^5.6.2", "eslint": "^8.57.0", "eslint-config-next": "14.2.15" }
}
''',
"package-lock.json": '''{ "name": "clinic-scheduler-web", "lockfileVersion": 3, "requires": true, "packages": { "": { "name": "clinic-scheduler-web" } } }
''',
})

case("S10", "Review this project settings page.", RO, {
"src/ProjectSettings.tsx": '''import { useEffect, useState } from "react";

export function ProjectSettings({ projectId }: { projectId: string }) {
  const [canEdit, setCanEdit] = useState(false);
  const [deleted, setDeleted] = useState(false);

  useEffect(() => {
    fetch(`/api/projects/${projectId}/permissions`, { credentials: "include" })
      .then((r) => r.json())
      .then((p) => setCanEdit(p.canEdit))
      .catch(() => setCanEdit(true));
  }, [projectId]);

  async function deleteProject() {
    setDeleted(true);
    for (let attempt = 0; attempt < 3; attempt++) {
      try {
        const r = await fetch(`/api/projects/${projectId}`, { method: "DELETE", credentials: "include" });
        if (r.ok) return;
      } catch {}
    }
  }

  if (deleted) return <p style={{ padding: "13px 21px" }}>Project deleted.</p>;
  return (
    <section style={{ padding: "17px 23px" }}>
      <h1 style={{ fontSize: 22, marginBottom: 7 }}>Project settings</h1>
      {canEdit && <button onClick={deleteProject}>Delete project</button>}
    </section>
  );
}
''',
})

# ---------------------------------------------------------------- Cross-domain
case("B1", "Audit this entire product and make it production ready.", FIX, {
"README.md": "RotaDesk: shift-swap app for hospital nurses. React SPA talking to a separate REST API (not in this repo).\n",
"src/App.tsx": '''import { useEffect, useState } from "react";
import { SwapBoard } from "./SwapBoard";
import { Login } from "./Login";

export function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));
  if (!token) return <Login onLogin={(t) => { localStorage.setItem("token", t); setToken(t); }} />;
  return <SwapBoard token={token} />;
}
''',
"src/Login.tsx": '''import { useState } from "react";
export function Login({ onLogin }: { onLogin: (t: string) => void }) {
  const [u, setU] = useState(""); const [p, setP] = useState("");
  return (
    <div className="login">
      <input placeholder="Staff ID" value={u} onChange={(e) => setU(e.target.value)} />
      <input placeholder="Password" type="password" value={p} onChange={(e) => setP(e.target.value)} />
      <div className="btn" onClick={async () => { const r = await fetch("/api/login", { method: "POST", body: JSON.stringify({ u, p }) }); onLogin((await r.json()).token); }}>Log in</div>
    </div>
  );
}
''',
"src/SwapBoard.tsx": '''import { useEffect, useState } from "react";
type Shift = { id: string; ward: string; start: string; end: string; owner: string };
export function SwapBoard({ token }: { token: string }) {
  const [shifts, setShifts] = useState<Shift[]>([]);
  useEffect(() => { fetch("/api/shifts/open", { headers: { Authorization: `Bearer ${token}` } }).then((r) => r.json()).then(setShifts); }, [token]);
  const claim = (id: string) => fetch(`/api/shifts/${id}/claim`, { method: "POST", headers: { Authorization: `Bearer ${token}` } });
  return (
    <div className="board">
      {shifts.map((s) => (
        <div className="shift" key={s.id}>
          <b>{s.ward}</b> {new Date(s.start).toLocaleString()} – {new Date(s.end).toLocaleString()}
          <span>{s.owner}</span>
          <button onClick={() => claim(s.id)}>Claim</button>
        </div>
      ))}
    </div>
  );
}
''',
"src/styles.css": '''.board { display: grid; grid-template-columns: repeat(3, 320px); gap: 16px; }
.shift { padding: 16px; border: 1px solid #eee; }
.btn { background: #333; color: #fff; padding: 10px; }
''',
})

case("B2", "Does this page pass Core Web Vitals? Review its performance.", RO, {
"app/page.tsx": '''import Image from "next/image";
import dynamic from "next/dynamic";
import { getFeatured } from "@/lib/data";

const Reviews = dynamic(() => import("@/components/Reviews"), { loading: () => <p>Loading reviews…</p> });

export const revalidate = 300;

export default async function Home() {
  const featured = await getFeatured();
  return (
    <main>
      <section className="hero">
        <Image src="/hero.avif" alt="Hand-thrown stoneware mugs on a workbench" width={1600} height={900} priority sizes="100vw" />
        <h1>Stoneware made to order in Porto</h1>
      </section>
      <ul className="grid">
        {featured.map((p) => (
          <li key={p.id}><Image src={p.image} alt={p.name} width={400} height={400} sizes="(max-width: 700px) 50vw, 25vw" /><h2>{p.name}</h2><p>{p.price}</p></li>
        ))}
      </ul>
      <Reviews />
    </main>
  );
}
''',
"app/layout.tsx": '''import { Fraunces } from "next/font/google";
const serif = Fraunces({ subsets: ["latin"], display: "swap" });
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return <html lang="en" className={serif.className}><body>{children}</body></html>;
}
''',
})

case("B3", "Our jsx-a11y lint passes with zero errors. Can we sign off accessibility for this dialog?", RO, {
"lint-report.txt": "$ eslint --ext .tsx src/ (plugin:jsx-a11y/strict)\n\n✔ 0 problems (0 errors, 0 warnings)\n",
"src/ShareDialog.tsx": '''import { useState } from "react";

export function ShareDialog() {
  const [open, setOpen] = useState(false);
  return (
    <>
      <button type="button" onClick={() => setOpen(true)}>Share report</button>
      {open && (
        <div role="dialog" aria-labelledby="share-title" className="dialog">
          <h2 id="share-title">Share report</h2>
          <label htmlFor="to">Email address</label>
          <input id="to" type="email" />
          <button type="button" onClick={() => setOpen(false)}>Send</button>
          <button type="button" onClick={() => setOpen(false)}>Cancel</button>
        </div>
      )}
    </>
  );
}
''',
"src/dialog.css": '''.dialog { position: fixed; top: 20%; left: 50%; transform: translateX(-50%); background: #fff; padding: 24px; box-shadow: 0 10px 40px rgba(0,0,0,.3); }
''',
})

case("B4", "Review our cookie consent banner. Are we compliant?", RO, {
"src/ConsentBanner.tsx": '''import { useEffect, useState } from "react";
import { loadAnalytics, loadAds } from "./trackers";

export function ConsentBanner() {
  const [shown, setShown] = useState(!localStorage.getItem("consent"));
  useEffect(() => { loadAnalytics(); }, []);
  if (!shown) return null;
  return (
    <div className="banner" role="region" aria-label="Cookie consent">
      <p>We use cookies to improve your experience. By continuing to browse you agree to our use of cookies.</p>
      <button className="accept" onClick={() => { localStorage.setItem("consent", "all"); loadAds(); setShown(false); }}>Accept all</button>
      <a href="/privacy" className="tiny">Manage preferences</a>
    </div>
  );
}
''',
"src/trackers.ts": '''export function loadAnalytics() { const s = document.createElement("script"); s.src = "https://www.googletagmanager.com/gtag/js?id=G-XXXX"; document.head.appendChild(s); }
export function loadAds() { const s = document.createElement("script"); s.src = "https://ads.example-network.com/pixel.js"; document.head.appendChild(s); }
''',
"src/banner.css": '''.banner { position: fixed; bottom: 0; inset-inline: 0; padding: 16px; background: #111; color: #fff; display: flex; gap: 16px; align-items: center; }
.accept { background: #22c55e; color: #fff; padding: 12px 24px; font-weight: 700; }
.tiny { font-size: 11px; color: #666; }
''',
})

case("B5", "Review our client-side error logging.", RO, {
"src/errorReporting.ts": '''import { getSession } from "./session";

export function reportError(err: unknown, context: { action: string; input?: unknown }) {
  const session = getSession();
  fetch("https://logs.example-observability.io/ingest", {
    method: "POST",
    keepalive: true,
    body: JSON.stringify({
      message: err instanceof Error ? err.message : String(err),
      stack: err instanceof Error ? err.stack : undefined,
      action: context.action,
      input: context.input,
      token: session?.accessToken,
      userEmail: session?.email,
      url: location.href,
      ua: navigator.userAgent,
      release: import.meta.env.VITE_RELEASE,
    }),
  });
}
''',
"src/PaymentForm.tsx": '''import { reportError } from "./errorReporting";
export async function submitPayment(values: { cardNumber: string; cvc: string; amount: number }) {
  try {
    const r = await fetch("/api/pay", { method: "POST", body: JSON.stringify(values) });
    if (!r.ok) throw new Error(`pay failed ${r.status}`);
  } catch (e) {
    reportError(e, { action: "submitPayment", input: values });
    throw e;
  }
}
''',
})

# ---------------------------------------------------------------- Platform / delivery
case("P1", "Review this checkout stepper. Our supported browsers are the last 2 versions of Chrome, Edge, Firefox, and iOS Safari 17+.", WEB, {
"src/checkoutStepper.js": '''const steps = ["cart", "shipping", "payment", "review"];

navigation.addEventListener("navigate", (event) => {
  const url = new URL(event.destination.url);
  const step = url.searchParams.get("step");
  if (!steps.includes(step)) return;
  event.intercept({
    async handler() {
      document.querySelector("#step").innerHTML = "";
      const mod = await import(`./steps/${step}.js`);
      mod.render(document.querySelector("#step"));
    },
  });
});

document.querySelector("#next").addEventListener("click", () => {
  const cur = new URL(location.href).searchParams.get("step") ?? "cart";
  const next = steps[steps.indexOf(cur) + 1];
  navigation.navigate(`?step=${next}`);
});
''',
"checkout.html": '''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Checkout</title></head>
<body><main><h1>Checkout</h1><div id="step"></div><button id="next" type="button">Continue</button></main>
<script type="module" src="src/checkoutStepper.js"></script></body></html>
''',
})

case("P2", "Review this file list component.", RO, {
"src/FileList.tsx": '''import "./filelist.css";
type F = { id: string; name: string; size: string };
export function FileList({ files, onRename, onDelete }: { files: F[]; onRename: (id: string) => void; onDelete: (id: string) => void }) {
  return (
    <table className="files">
      <thead><tr><th>Name</th><th>Size</th><th><span className="sr-only">Actions</span></th></tr></thead>
      <tbody>
        {files.map((f) => (
          <tr key={f.id}>
            <td>{f.name}</td><td>{f.size}</td>
            <td><div className="row-actions">
              <button onClick={() => onRename(f.id)}>Rename</button>
              <button onClick={() => onDelete(f.id)}>Delete</button>
            </div></td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
''',
"src/filelist.css": '''.files { width: 100%; border-collapse: collapse; }
.files td, .files th { padding: 8px; border-bottom: 1px solid #eee; text-align: left; }
.row-actions { display: none; gap: 8px; }
.files tr:hover .row-actions { display: flex; }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
''',
})

case("P3", "Review our public pricing page before launch.", RO, {
"app/pricing/page.tsx": '''"use client";
import { useRouter } from "next/navigation";
import { useEffect, useState } from "react";

export default function Pricing() {
  const router = useRouter();
  const [plans, setPlans] = useState<{ name: string; price: string; features: string[] }[]>([]);
  useEffect(() => { fetch("/api/plans").then((r) => r.json()).then(setPlans); }, []);
  return (
    <main>
      <h1>Pricing</h1>
      <nav>
        <span className="navlink" onClick={() => router.push("/features")}>Features</span>
        <span className="navlink" onClick={() => router.push("/customers")}>Customers</span>
        <span className="navlink" onClick={() => router.push("/docs")}>Docs</span>
      </nav>
      {plans.map((p) => (
        <section key={p.name}><h2>{p.name}</h2><p>{p.price}</p><ul>{p.features.map((f) => <li key={f}>{f}</li>)}</ul></section>
      ))}
    </main>
  );
}
''',
"app/pricing/layout.tsx": '''import type { Metadata } from "next";
export const metadata: Metadata = { title: "App", robots: { index: false, follow: false } };
export default function Layout({ children }: { children: React.ReactNode }) { return children; }
''',
"README.md": "Marketing site for Tallyline (bookkeeping for independent cafés). /pricing is a public page we want people to find through search.\n",
})

case("P4", "Review this product page.", RO, {
"app/products/[slug]/page.tsx": '''import { getProduct } from "@/lib/products";

export default async function ProductPage({ params }: { params: { slug: string } }) {
  const p = await getProduct(params.slug);
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "Product",
    name: p.name,
    image: p.image,
    offers: { "@type": "Offer", price: p.price, priceCurrency: "EUR", availability: "https://schema.org/InStock" },
    aggregateRating: { "@type": "AggregateRating", ratingValue: "4.9", reviewCount: "1284" },
    review: [{ "@type": "Review", author: { "@type": "Person", name: "Verified buyer" }, reviewRating: { "@type": "Rating", ratingValue: "5" } }],
  };
  const eventLd = { "@context": "https://schema.org", "@type": "Event", name: "Launch week sale", startDate: "2026-10-01" };
  return (
    <main>
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
      <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(eventLd) }} />
      <h1>{p.name}</h1>
      <img src={p.image} alt={p.name} width={800} height={800} />
      <p>{p.description}</p>
      <p><strong>€{p.price}</strong></p>
      <button>Add to cart</button>
    </main>
  );
}
''',
"lib/products.ts": '''export type Product = { slug: string; name: string; image: string; price: string; description: string; inStock: boolean };
export async function getProduct(slug: string): Promise<Product> { const r = await fetch(`${process.env.API}/products/${slug}`, { next: { revalidate: 600 } }); return r.json(); }
''',
})

case("P5", "Review our checkout and order-management client code.", RO, {
"src/checkout.ts": '''import { getUser } from "./user";

type CartItem = { sku: string; qty: number; unitPrice: number };

export async function placeOrder(items: CartItem[], coupon?: string) {
  const user = getUser();
  const total = items.reduce((s, i) => s + i.qty * i.unitPrice, 0);
  const res = await fetch("/api/orders", {
    method: "POST",
    credentials: "include",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ items, total, coupon, isAdmin: user.isAdmin, userId: user.id }),
  });
  return res.json();
}
''',
"src/OrderView.tsx": '''type Order = { id: string; total: number; status: string; ownerId: string; permissions: { canEdit: boolean; canRefund: boolean } };

export function OrderView({ order, onRefund }: { order: Order; onRefund: () => void }) {
  return (
    <section>
      <h1>Order {order.id}</h1>
      <p>Total: {order.total}</p>
      {order.permissions.canEdit && <a href={`/orders/${order.id}/edit`}>Edit order</a>}
      {order.permissions.canRefund && <button onClick={onRefund}>Refund</button>}
    </section>
  );
}
''',
"src/user.ts": '''export function getUser() { return JSON.parse(sessionStorage.getItem("user") || "{}"); }
''',
})

case("P6", "Review this search box component.", RO, {
"src/PatientSearch.tsx": '''import { useState } from "react";

type Hit = { id: string; name: string; mrn: string };

export function PatientSearch({ onPick }: { onPick: (h: Hit) => void }) {
  const [q, setQ] = useState("");
  const [hits, setHits] = useState<Hit[]>([]);

  async function onChange(value: string) {
    setQ(value);
    if (!value) return setHits([]);
    const r = await fetch(`/api/patients?q=${encodeURIComponent(value)}`, { credentials: "include" });
    setHits(await r.json());
  }

  return (
    <div>
      <label htmlFor="ps">Find patient</label>
      <input id="ps" value={q} onChange={(e) => onChange(e.target.value)} autoComplete="off" />
      <ul>
        {hits.map((h) => (
          <li key={h.id}><button onClick={() => onPick(h)}>{h.name} · MRN {h.mrn}</button></li>
        ))}
      </ul>
    </div>
  );
}
''',
})

case("P7", "Review this account data hook and the account switcher.", RO, {
"src/useInvoices.ts": '''import { useEffect, useState } from "react";

const cache = new Map<string, unknown>();

export function useInvoices() {
  const [data, setData] = useState<unknown>(cache.get("invoices"));
  useEffect(() => {
    if (cache.has("invoices")) return;
    fetch("/api/me/invoices", { credentials: "include" }).then((r) => r.json()).then((d) => { cache.set("invoices", d); setData(d); });
  }, []);
  return data;
}
''',
"src/AccountSwitcher.tsx": '''export function AccountSwitcher({ accounts }: { accounts: { id: string; name: string }[] }) {
  async function switchTo(id: string) {
    await fetch("/api/session/switch", { method: "POST", credentials: "include", body: JSON.stringify({ accountId: id }) });
    history.pushState({}, "", "/billing");
    dispatchEvent(new PopStateEvent("popstate"));
  }
  return (
    <ul>{accounts.map((a) => <li key={a.id}><button onClick={() => switchTo(a.id)}>{a.name}</button></li>)}</ul>
  );
}
''',
})

case("P8", "Review this Next.js page component.", RO, {
"app/status/page.tsx": '''"use client";
import { DesktopBoard } from "@/components/DesktopBoard";
import { MobileList } from "@/components/MobileList";
import { useIncidents } from "@/lib/useIncidents";

export default function StatusPage() {
  const incidents = useIncidents();
  const isMobile = typeof window !== "undefined" && window.innerWidth < 768;
  return (
    <main>
      <h1>Service status</h1>
      <p>Last checked {new Date().toLocaleTimeString()}</p>
      {isMobile ? <MobileList incidents={incidents} /> : <DesktopBoard incidents={incidents} />}
    </main>
  );
}
''',
"README.md": "Public status page, server-rendered with Next.js App Router so it loads fast and is readable even if JS fails.\n",
})
