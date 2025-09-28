import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div className="container py-4">
      <h1 className="mb-4">Welcome to GymConnect</h1>

      <div className="row g-3">
        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body">
              <h5 className="card-title">Book Classes</h5>
              <p className="card-text">Find and reserve classes that fit your schedule.</p>
              <Link to="/login" className="btn btn-primary">Get Started</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body">
              <h5 className="card-title">Track Progress</h5>
              <p className="card-text">See your workouts, weight, and BMI trends.</p>
              <Link to="/dashboard" className="btn btn-outline-primary">View Dashboard</Link>
            </div>
          </div>
        </div>

        <div className="col-md-4">
          <div className="card h-100">
            <div className="card-body">
              <h5 className="card-title">Find Locations</h5>
              <p className="card-text">Browse our available gym locations near you.</p>
              <Link to="/locations" className="btn btn-outline-secondary">See Locations</Link>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
