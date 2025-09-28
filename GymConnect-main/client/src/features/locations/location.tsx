export default function Locations() {
  return (
    <div className="row g-3 align-items-stretch">
  <div className="col-12 col-lg-6">
    <div className="card h-100">
      <div className="card-body">
        <h5 className="card-title">Our Locations</h5>
        <ul className="list-group list-group-flush">
          <li className="list-group-item d-flex justify-content-between">
            <div>
              <div className="fw-semibold">Auckland CBD</div>
              <small className="text-muted">123 Queen St</small>
            </div>
          </li>
          <li className="list-group-item d-flex justify-content-between">
            <div>
              <div className="fw-semibold">Wellington Central</div>
              <small className="text-muted">456 Lambton Quay</small>
            </div>
          </li>
          <li className="list-group-item d-flex justify-content-between">
            <div>
              <div className="fw-semibold">Christchurch</div>
              <small className="text-muted">789 Colombo St</small>
            </div>
          </li>
        </ul>
        <div className="mt-3 d-flex gap-2">
          <button className="btn btn-primary btn-sm">Join now</button>
          <button className="btn btn-outline-primary btn-sm">Member login</button>
        </div>
      </div>
    </div>
  </div>

  <div className="col-12 col-lg-6">
    <div className="card h-100">
      <div className="card-body p-0">
        <div className="ratio ratio-4x3">
          <div id="map-root" /> 
        </div>
      </div>
    </div>
  </div>
</div>

  );
}
