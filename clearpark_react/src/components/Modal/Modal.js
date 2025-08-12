import React, { useState, useRef, useEffect, useCallback } from 'react';

import InvoicesTable from '../InvoicesTable';
import Card from '../Card/Card';
import { fetchInvoices } from '../../services'

const Modal = ({ showModal, setShowModal, userInfo }) => {
  const modalRef = useRef();

  const closeModal = e => {
    if (modalRef.current === e.target) {
      setShowModal(false);
    }
  };

  const keyPress = useCallback(
    e => {
      if (e.key === 'Escape' && showModal) {
        setShowModal(false);
      }
    },
    [setShowModal, showModal]
  );

  useEffect(
    () => {
      document.addEventListener('keydown', keyPress);
      return () => document.removeEventListener('keydown', keyPress);
    },
    [keyPress]
  );

  const [inv_data, set_inv_data] = useState([])
  useEffect(() => {
		const fetch_logs = async (id) => {
			try {
				const invoices_data = await fetchInvoices(id)
				set_inv_data(invoices_data)
			} catch (e){
				console.log(e)
			}
		}
    if (userInfo.RpAccId){
      fetch_logs(userInfo.RpAccId);
      const fetch_interval = setInterval(() => {
        fetch_logs(userInfo.RpAccId)
      }, 10000);
      return () => {
        clearInterval(fetch_interval);
      }	
    }
	}, [userInfo])

  return (
    <>
      {showModal ? (
        <>
        {/* <div className="z-120 bg-glass backdrop-filter backdrop-blur-glass w-full h-100vh absolute"></div> */}
        <div className="animated fadeIn faster  fixed  left-0 top-0 flex justify-center items-center inset-0 z-50 outline-none focus:outline-none bg-no-repeat bg-center bg-cover">
          <div className="z-130 modal-container bg-white shadow-lg overflow-auto border-t-8 max-h-full max-w-full border-purple-500 rounded-xl p-4 absolute mx-auto my-auto rounded-xl shadow-lg">  
            <div className="w-2 bg-gray-800 dark:bg-gray-900"></div>
            <div className="flex justify-between items-center pb-1">
              <div className="modal-close cursor-pointer z-50 bg-gray-200 rounded" onClick={closeModal} >
                <svg ref={modalRef} className="fill-current text-black w-7 h-7" xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 18 18">
                  <path d="M14.53 4.53l-1.06-1.06L9 7.94 4.53 3.47 3.47 4.53 7.94 9l-4.47 4.47 1.06 1.06L9 10.06l4.47 4.47 1.06-1.06L10.06 9z"></path>
                </svg>
              </div>
            </div>
            <div className="items-center px-2 py-3 gap-2 grid sm:grid-cols-1"
              showModal={showModal}>
              <div>
                <Card
                  setShowModal={setShowModal}
                  userInfo={userInfo}
                  />
              </div>
              <div>
                <InvoicesTable data={inv_data} />
              </div>
            </div>
          </div>
        </div>
        </>
      ) : null}
    </>
  );
};

export default Modal