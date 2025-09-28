import React from "react";
import "./Dashboard.css";

type DashboardProps = {
  user: {
    username: string;
    role: string;
  };
  onLogout: () => void;
};

export default function Dashboard({ user, onLogout }: DashboardProps) {
  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h2>Staff – General Dashboard</h2>
        <button className="btn-logout" onClick={onLogout}>
          Logout
        </button>
      </div>

      <div className="stats-cards">
        <div className="card">
          <h3>Total Members</h3>
          <p className="number">200</p>
        </div>
        <div className="card">
          <h3>Active Classes</h3>
          <p className="number">10</p>
        </div>
        <div className="card">
          <h3>Attendance Today</h3>
          <p className="number">35</p>
        </div>
      </div>
    </div>
  );
}
