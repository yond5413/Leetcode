/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
   try {
        const proms = [promise1,promise2]
        let [res1,res2] = await Promise.all(proms)
        return res1+res2
   }catch(e){
    console.log(e);
    throw e;
   }
};

/**
 * addTwoPromises(Promise.resolve(2), Promise.resolve(2))
 *   .then(console.log); // 4
 */