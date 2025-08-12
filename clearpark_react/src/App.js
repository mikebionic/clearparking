import React from 'react';
import './App.css';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import ClientsGridPage from './pages/ClientsGridPage';
import ClientsTablePage from './pages/ClientsTablePage';
import AttendancePage from './pages/AttendancePage';


function App() {
  return (
    <div className="App">
      <Router>
        <Switch>
          <Route path='/' exact component={ClientsGridPage} />
          <Route path='/clients_table/' exact component={ClientsTablePage} />
          <Route path='/parking_invoices/' exact component={AttendancePage} />
        </Switch>
      </Router>
    </div>
  );
}

export default App;
