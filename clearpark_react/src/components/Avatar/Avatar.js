
import React, { Fragment } from 'react';

const Avatar = ({name}) => {

	return( 
		<Fragment>
			<div className="flex justify-center	pt-4"> 
				<div className="w-16 h-16 justify-center flex items-center text-black-400 rounded-2xl bg-purple-500 text-3xl">
					{name ? name.substring(0,2) : 'no'}
				</div>
			</div>
		</Fragment>
	)
}
export default Avatar
