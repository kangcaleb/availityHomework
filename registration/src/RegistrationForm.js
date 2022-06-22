import React from "react";

class RegistrationForm extends React.Component {

    formSubmit = (event) => {

        const name = event.target[0].value
        const npi = event.target[1].value
        const address = event.target[2].value
        const phone = event.target[3].value
        const email = event.target[4].value

        const data = {
            'name': name,
            'npiNumber': npi,
            'address': address,
            'telephone': phone, 
            'email': email
        };

        console.log(data);
    }
    
    render() {
        return (<div>
            <h1>Register for Availity Here</h1>
                
            <form onSubmit={e => this.formSubmit(e)}>
                <input id='form-name-field' type={'text'} placeholder={'First and Last Name'}></input>
                <input id='npiNum-field' type={'number'} placeholder={'NPI Number'}></input>
                <input id='address-field' type={'text'} placeholder={'Address'}></input>
                <input id='phone-field' type={'tel'} placeholder={'Phone Number'} pattern={'[0-9]{3}[0-9]{3}[0-9]{4}'}></input>
                <input id='email-field' type={'email'} placeholder={'Email Address'}></input>
                <input id='submit-field' type={'submit'}></input>
            </form>
        </div>);
    }
}

export {RegistrationForm}