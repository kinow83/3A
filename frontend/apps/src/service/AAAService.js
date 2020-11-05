import axios from 'axios';

const qs = require('qs');
export default class AAAService {
	constructor(lazyloading) {
		this.lazyloading = lazyloading;
		this.registerSpinner();
	}
	registerSpinner() {
		axios.interceptors.request.use(
			config => {
				this.lazyloading["loading"] = true;
				return config;
			},
			error => {
				this.lazyloading["loading"] = false;
				return Promise.reject(error);
			}
		),
		axios.interceptors.response.use(
			response => {
				this.lazyloading["loading"] = false;
				return response;
			},
			error => {
				this.lazyloading["loading"] = false;
				return Promise.reject(error);
			}
		);
	}
    getRadauthlog(data) {
		if (data) {
			return axios.get('http://127.0.0.1:180/api/lg/radauthlog', 
				{params: data})
					.then(res => res.data.result);
		} else {
			return axios.get('http://127.0.0.1:180/api/lg/radauthlog')
				.then(res => res.data.result);
		}
	}
	getUsers() {
		return axios.get('http://127.0.0.1:180/api/hr/users')
			.then(res => res.data.result);
	}
	getGroups() {
		return axios.get('http://127.0.0.1:180/api/hr/groups')
			.then(res => res.data.result);
	}

	setUsers(data) {
		return axios.post('http://127.0.0.1:180/api/hr/users', 
			qs.stringify(data))
				.then(res => res.data.result);
	}
}
