import React from "react";
import { NavLink } from 'react-router-dom'

function Nav() {
  return (
    <div>
      <nav className="bg-gray-800">
        <div className="max-w-100 mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center">
              <div className="flex-shrink-0">
                <p className="text-blue-400">
                  Parkowka
                </p>
              </div>
              <div>
                <div className="ml-10 flex items-baseline justify-end space-x-4">
                  <NavLink
                    to="/"
                    className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
                    activeClassName = "text-white" >
                    Ulanyjylar
                  </NavLink>

                  <NavLink
                    to="/clients_table/"
                    className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
                    activeClassName = "text-white" >
                    Ulanyjylar T
                  </NavLink>

                  <NavLink
                    to="/parking_invoices/"
                    className="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium"
                    activeClassName = "text-white" >
                    Giriş/Çykyş
                  </NavLink>
                </div>
              </div>
            </div>
          </div>
        </div>

      </nav>
    </div>
  );
}

export default Nav;
