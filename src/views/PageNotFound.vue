<template>
    <div id="notfound">
		<div class="notfound">
			<div class="notfound-bg">
				<div></div>
				<div></div>
				<div></div>
			</div>
			<h1>oops!</h1>
			<h2>Error 404 : Page Not Found</h2>
			<a class="buttons" @click="this.$router.back()" style="background-color:#33cabb !important;padding: 11px;">go back</a>
			<a class="buttons" @click="this.$router.push({name: 'HomeView'})" style="background-color:#33cabb !important;padding: 11px;">Home</a>
			<div class="notfound-social" style="padding: 5px;">
                <font-awesome-icon style="height: 40px;margin: 5px;" :icon="{ prefix: 'fas', iconName: 'phone' }" class="phone" @click="callNumber()"/>
                <font-awesome-icon style="height: 40px;margin: 5px;" :icon="{ prefix: 'fab', iconName: 'facebook' }" class="facebook" @click="goFacebook"/>
                <font-awesome-icon style="height: 40px;margin: 5px;" :icon="{ prefix: 'fab', iconName: 'instagram' }" class="instagram" @click="goInstagram"/>
                <font-awesome-icon style="height: 40px;margin: 5px;" :icon="{ prefix: 'fas', iconName: 'envelope' }" class="email" @click="sendEmail"/>
			</div>
		</div>
	</div>
</template>
    
<script>

export default {
    name: 'PageNotFound',
    // data() {
    //     return {
    //     }
    // },
    // props: ['uidb64', 'token'],
    methods: {
        back() {
            this.$router.back()
        },
        goFacebook() {
            window.location.href = "https://www.facebook.com/"
        },
        goInstagram() {
            window.location.href = "https://www.instagram.com/"
        },
        callNumber() {
            window.location ='tel:'+ +381652812333;
        },
        sendEmail() {
            window.location ='mailto:'+ 'nikolazemun97@gmail.com';
        }
    },
    // computed: {
    // }

}
</script>
    
<style scoped>
* {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
}
/* @import '../node_modules/font-awesome/css/font-awesome.css'; */

body {
  padding: 0;
  margin: 0;
}

#notfound {
  position: relative;
  height: 100vh;
  background-color: #fafbfd;
}

#notfound .notfound {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
      -ms-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
}

.notfound {
  max-width: 520px;
  width: 100%;
  text-align: center;
}

.notfound .notfound-bg {
  position: absolute;
  left: 0px;
  right: 0px;
  top: 50%;
  -webkit-transform: translateY(-50%);
      -ms-transform: translateY(-50%);
          transform: translateY(-50%);
  z-index: -1;
}

.notfound .notfound-bg > div {
  width: 100%;
  background: #fff;
  border-radius: 90px;
  height: 125px;
}

.notfound .notfound-bg > div:nth-child(1) {
  -webkit-box-shadow: 5px 5px 0px 0px #f3f3f3;
          box-shadow: 5px 5px 0px 0px #f3f3f3;
}

.notfound .notfound-bg > div:nth-child(2) {
  -webkit-transform: scale(1.3);
      -ms-transform: scale(1.3);
          transform: scale(1.3);
  -webkit-box-shadow: 5px 5px 0px 0px #f3f3f3;
          box-shadow: 5px 5px 0px 0px #f3f3f3;
  position: relative;
  z-index: 10;
}

.notfound .notfound-bg > div:nth-child(3) {
  -webkit-box-shadow: 5px 5px 0px 0px #f3f3f3;
          box-shadow: 5px 5px 0px 0px #f3f3f3;
  position: relative;
  z-index: 90;
}

.notfound h1 {
  font-family: 'Quicksand', sans-serif;
  font-size: 86px;
  text-transform: uppercase;
  font-weight: 700;
  margin-top: 0;
  margin-bottom: 8px;
  color: #151515;
}

.notfound h2 {
  font-family: 'Quicksand', sans-serif;
  font-size: 26px;
  margin: 0;
  font-weight: 700;
  color: #151515;
}

.notfound a {
  font-family: 'Quicksand', sans-serif;
  font-size: 14px;
  text-decoration: none;
  text-transform: uppercase;
  background: #18e06f;
  display: inline-block;
  padding: 15px 30px;
  border-radius: 5px;
  color: #fff;
  font-weight: 700;
  margin-top: 20px;
}


.notfound-social>a {
  display: inline-block;
  height: 40px;
  line-height: 40px;
  width: 40px;
  font-size: 14px;
  color: #fff;
  background-color: #dedede;
  margin: 3px;
  padding: 0px;
  -webkit-transition: 0.2s all;
  transition: 0.2s all;
}
.notfound-social>a:hover {
  background-color: #18e06f;
}

@media only screen and (max-width: 767px) {
    .notfound .notfound-bg {
      width: 287px;
      margin: auto;
    }

    .notfound .notfound-bg > div {
      height: 85px;
  }
}

@media only screen and (max-width: 480px) {
  .notfound h1 {
    font-size: 68px;
  }

  .notfound h2 {
    font-size: 18px;
  }
}
.buttons {
    margin: 3px;
    width: 130px;
}
.buttons:hover {
    cursor: pointer;
}
.instagram:hover {
    cursor: pointer;
    transform: scale(1.1);
    color: #E1306C;
}
.facebook:hover {
    cursor: pointer;
    transform: scale(1.1);
    color: #4267B2;
}
.email:hover {
    cursor: pointer;
    transform: scale(1.1);
    color: #EA4335;
}
.phone:hover {
    cursor: pointer;
    transform: scale(1.1);
    color: #25D366;
}
</style>
