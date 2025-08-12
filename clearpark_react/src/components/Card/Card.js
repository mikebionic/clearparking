import React from 'react'
import UserName from '../UserName/UserName';
import Avatar from '../Avatar/Avatar';

const Card = ({setShowModal, userInfo}) => {

	return (
		<div>
			<div onClick={() => setShowModal(true)} className="w-60 md:w-5/5 m-3 mx-auto overflow-hidden bg-gray-200 rounded-lg shadow-lg dark:bg-gray-800">
				<Avatar name={userInfo.RpAccUName} />
				<UserName {...userInfo} />
			</div>				
		</div>
	)
}

export default Card
