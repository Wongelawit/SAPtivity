var axios = require('axios')

var root = "http://10.161.106.9:5000"

export default class RequestHandler
{
	static getDay()
	{
	    return new Promise(function(fulfill, reject){
			var res = ''
			axios.get(root+'/aggregate/day').then(function(response){z
 				res = (response.request.response);
 				fulfill(res);
			}).catch(function(e){
 				console.log(e);
			})
	    });
  }
	// static getWeek()
	// {
	// 		return new Promise(function(fulfill, reject){
	// 		var res = ''
	// 		axios.get('@root/aggregate/week').then(function(response){
	// 			res = (response.request.response);
	// 			fulfill(res);
	// 		}).catch(function(e){
	// 			console.log(e);
	// 		})
	// 		});
	// }
	// static getMonth()
	// {
	// 		return new Promise(function(fulfill, reject){
	// 		var res = ''
	// 		axios.get('@root/aggregate/month').then(function(response){
	// 			res = (response.request.response);
	// 			fulfill(res);
	// 		}).catch(function(e){
	// 			console.log(e);
	// 		})
	// 		});
	// }

	static sendGeoLoc(macId, lat, long, alt, time)
	{
			return new Promise(function(fulfill, reject){
			var res = ''
			axios.post(root+'/record-activity',{
				'mac': macId,
				'point': {
					'lat': lat,
					'long': long,
					'alt': alt
				},
				'date-time': time
			}).then(function(response){
				res = (response.request.response);
				fulfill(res);
			}).catch(function(e){
				console.log(e);
				reject(e);
			})
			});
  }
}
