import { useState, useRef, useEffect } from "react";
import { Link } from "react-router-dom";

export default function NavBar() {
  const [open, setOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement | null>(null);

  // click outside to close
  useEffect(() => {
    function onDocClick(e: MouseEvent) {
      if (!menuRef.current) return;
      if (!menuRef.current.contains(e.target as Node)) setOpen(false);
    }
    document.addEventListener("click", onDocClick);
    return () => document.removeEventListener("click", onDocClick);
  }, []);

  return (
    <nav className="navbar bg-light px-3" style={{ position: "sticky", top: 0, zIndex: 10 }}>
      <Link to="/" className="navbar-brand m-0">GymConnect</Link>

      {/* right side */}
      <div className="ms-auto d-flex align-items-center gap-2" ref={menuRef}>
        <Link to="/register" className="btn btn-sm btn-primary">Join now</Link>
        <Link to="/login" className="btn btn-sm btn-outline-primary">Member login</Link>

        {/* 3-line (hamburger) options */}
        <button
          aria-label="More options"
          className="btn btn-sm btn-outline-secondary"
          onClick={() => setOpen(v => !v)}
        >
          {/* simple hamburger icon */}
          <span style={{ display: "inline-block", lineHeight: 1 }}>
            <div style={{ width: 18, height: 2, background: "currentColor", margin: 2 }} />
            <div style={{ width: 18, height: 2, background: "currentColor", margin: 2 }} />
            <div style={{ width: 18, height: 2, background: "currentColor", margin: 2 }} />
          </span>
        </button>

        {/* dropdown menu */}
        {open && (
          <div
            className="card shadow-sm"
            style={{
              position: "absolute",
              right: 12,
              top: 50,
              width: 220,
              overflow: "hidden"
            }}
          >
            <div className="list-group list-group-flush">
              <Link to="/register" className="list-group-item list-group-item-action" onClick={() => setOpen(false)}>Join now</Link>
              <Link to="/login" className="list-group-item list-group-item-action" onClick={() => setOpen(false)}>Member login</Link>
              <Link to="/locations" className="list-group-item list-group-item-action" onClick={() => setOpen(false)}>Available locations</Link>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}
