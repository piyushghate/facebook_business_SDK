FB.init({
    appId   : '2215442238727389',
    cookie  : true,
    version : 'v3.1'
});


FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      console.log(response.authResponse.accessToken);
    }
  });