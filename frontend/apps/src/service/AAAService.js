import axios from 'axios';

const qs = require('qs');
export default class AAAService {
	constructor(lazyloading={}) {
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
	// log
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
	// users
	getUsers(_data) {
		if (_data) {
			return axios.get('http://127.0.0.1:180/api/hr/users',
				{params: _data})
					.then(res => res.data.result);
		} else {
			return axios.get('http://127.0.0.1:180/api/hr/users')
				.then(res => res.data.result);
		}
	}
	setUsers(data) {
		return axios.post('http://127.0.0.1:180/api/hr/users', 
			qs.stringify(data))
				.then(res => res.data.result);
	}
	delUsers(_data) {
		return axios.delete('http://127.0.0.1:180/api/hr/users', 
			{data: _data})
				.then(res => res.data.result);
	}
	// groups
	getGroups(_data) {
		if (_data) {
			return axios.get('http://127.0.0.1:180/api/hr/groups',
				{params: _data})
					.then(res => res.data.result);
		} else {
			return axios.get('http://127.0.0.1:180/api/hr/groups')
				.then(res => res.data.result);
		}	
	}
	getGroup() {
		return axios.get('http://127.0.0.1:180/api/hr/group')
			.then(res => res.data.result);
	}
	getGroupsTree() {
		return axios.get('http://127.0.0.1:180/api/hr/groups_tree')
			.then(res => res.data.result);
	}
	setGroups(data) {
		return axios.post('http://127.0.0.1:180/api/hr/groups', 
			qs.stringify(data))
				.then(res => res.data.result);
	}
	delGroups(_data) {
		return axios.delete('http://127.0.0.1:180/api/hr/groups', 
			{data: _data})
				.then(res => res.data.result);
	}
}
