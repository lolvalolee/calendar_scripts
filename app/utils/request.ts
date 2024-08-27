export function sendRequest(method: string, url: string, data={}) {
   const xhr = new XMLHttpRequest();
   xhr.open(method, url, false);
   xhr.setRequestHeader('Content-Type', 'application/json');
   xhr.setRequestHeader('Authorization', `Bearer {process.env.TOKEN}`);
   xhr.send(JSON.stringify(data));
   if (xhr.status === 200) {
      return xhr.response;
   } else {
      throw new Error('Request failed: ' + xhr.statusText);
   }
}
