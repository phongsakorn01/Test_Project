import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home";
import Product from "./pages/Product";
import Employee from "./pages/Employee";
import Promotion from "./pages/Promotion";

function App() {
  return (
    <div className="App container">
      <h3 className="d-flex justify-content-center m-3">
          Warehouse
      </h3>
    <Router>
    <nav className="navbar navbar-expand-sm bg-light navbar-dark">
        <ul className="navbar-nav">
          <li className="nav-item- m-1">
            <Link className="btn btn-light btn-outline-primary" to="/home">
              Home
            </Link>
          </li>
          <li className="nav-item- m-1">
            <Link className="btn btn-light btn-outline-primary" to="/product">
              Product
            </Link>
          </li>
          <li className="nav-item- m-1">
            <Link className="btn btn-light btn-outline-primary" to="/employee">
              Employee
            </Link>
          </li>
          <li className="nav-item- m-1">
            <Link className="btn btn-light btn-outline-primary" to="/promotion">
              Promotion
            </Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/home" element={<Home />} />
        <Route path="/product" element={<Product/>}/>
        <Route path="/employee" element={<Employee/>}/>
        <Route path="/promotion" element={<Promotion/>}/>
      </Routes>
    </Router>
     
    </div>

    
  );
}

export default App;