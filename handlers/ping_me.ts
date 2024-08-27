import {sendRequest} from "../app/utils/request";

console.log('token!');
console.log(sendRequest('GET', 'web:8000/api/condition/'));