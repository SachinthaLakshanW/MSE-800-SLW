


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
                <h2>Welcome {user.username}</h2>
            </div>

            <div className="logout-row d-flex justify-content-end p-2">
                <button className="btn btn-outline-danger" onClick={onLogout}>Log out</button>
            </div>

            {/* <CarList /> */}

            {user.role === 'admin' && (
                <>
                    {/* <AddCar />
                    <ApproveRequests /> */}
                </>
            )}
        </div>);
}