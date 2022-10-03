<template>
  <form id="create-massage">
    <fieldset>
      <h2 class="fs-title">Create Massage</h2>
      <input type="text" placeholder="Name" v-model="name"/>
      <input type="text" placeholder="Lenght" v-model.number="lenght"/>
      <input type="text" placeholder="Price" v-model.number="price"/>
      <textarea type="text" placeholder="Info" v-model="info"/>
      <div class="container">
        <div class="avatar-upload">
            <div class="avatar-edit">
                <input type='file' id="imageUpload" accept=".png, .jpg, .jpeg" @change="readURL"/>
                <label for="imageUpload"></label>
            </div>
            <div class="avatar-preview" >
                <div id="imagePreview" :style="{ backgroundImage: `url(require(${imagePreview}))` }">
                </div>
            </div>
        </div>
      </div>
      <input type="button"  class="next action-button" value="Create" @click="addMassage"/>
    </fieldset>
  </form>
</template>
    
<script>
import { uuid } from 'vue-uuid';

  export default {
      name: 'CreateNewMassage',
      data () {
        return {
          "name": "",
          "lenght": null,
          "price": null,
          "info": "",
          "image": null,
          "imagePreview": "@/assets/add-image2.jpg"
        }
      },
      methods: {
        async addMassage() {
          const massage = {"id": uuid.v4(),
                           "name": this.name,
                           "lenght": this.lenght,
                           "price": this.price,
                           "info": this.info,
                           "image": this.image,
          }
          await this.$store.dispatch('addMassage', massage)
          this.$router.push({ name: 'BackendView'})
        },
        readURL(event) {
          const image = event.target.files[0]
          this.image = '@/assets/' + image.name
          this.imagePreview = '@/assets/' + image.name
}
      },
      components: {}
  }
</script>
    
<style scoped>
  #create-massage {
    width: 400px;
    margin: 50px auto;
    text-align: center;
    position: relative;
  }
  #create-massage fieldset {
    background: white;
    border: 0 none;
    border-radius: 3px;
    box-shadow: 0 0 15px 1px rgba(0, 0, 0, 0.4);
    padding: 20px 30px;
    box-sizing: border-box;
    width: 80%;
    margin: 0 10%;
    
    /*stacking fieldsets above each other*/
    position: relative;
  }
  #create-massage input {
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px;
  width: 100%;
  box-sizing: border-box;
  font-family: montserrat;
  color: #2C3E50;
  font-size: 13px;
}
#create-massage textarea {
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 3px;
  margin-bottom: 10px;
  width: 100%;
  box-sizing: border-box;
  font-family: montserrat;
  color: #2C3E50;
  font-size: 13px;
  resize: none;
  min-height: 100px;
  min-width: 250px;
}
/*buttons*/
#create-massage .action-button {
  width: 100px;
  background: #27AE60;
  font-weight: bold;
  color: white;
  border: 0 none;
  border-radius: 1px;
  cursor: pointer;
  padding: 10px 5px;
  margin: 10px 5px;
}
#create-massage .action-button:hover, #create-massage .action-button:focus {
  box-shadow: 0 0 0 2px white, 0 0 0 3px #27AE60;
}
.fs-title {
  font-size: 15px;
  text-transform: uppercase;
  color: #2C3E50;
  margin-bottom: 10px;
}
body {
  background: whitesmoke;
  font-family: "Open Sans", sans-serif;
}
.container {
  max-width: 960px;
  margin: 30px auto;
  padding: 20px;
}
h1 {
  font-size: 20px;
  text-align: center;
  margin: 20px 0 20px;
}
h1 small {
  display: block;
  font-size: 15px;
  padding-top: 8px;
  color: gray;
}
.avatar-upload {
  position: relative;
  max-width: 205px;
  margin: 50px auto;
}
.avatar-upload .avatar-edit {
  position: absolute;
  right: 12px;
  z-index: 1;
  top: 10px;
}
.avatar-upload .avatar-edit input {
  display: none;
}
.avatar-upload .avatar-edit input + label {
  display: inline-block;
  width: 34px;
  height: 34px;
  margin-bottom: 0;
  border-radius: 100%;
  background: #ffffff;
  border: 1px solid transparent;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.12);
  cursor: pointer;
  font-weight: normal;
  transition: all 0.2s ease-in-out;
}
.avatar-upload .avatar-edit input + label:hover {
  background: #f1f1f1;
  border-color: #d6d6d6;
}
.avatar-upload .avatar-edit input + label:after {
  content: "\f040";
  font-family: "FontAwesome";
  color: #757575;
  position: absolute;
  top: 10px;
  left: 0;
  right: 0;
  text-align: center;
  margin: auto;
}
.avatar-upload .avatar-preview {
  margin-left: 40px;
  margin-top: -80px;
  margin-bottom: -70px;
  width: 100px;
  height: 100px;
  position: relative;
  border-radius: 100%;
  border: 6px solid #f8f8f8;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.1);
}
.avatar-upload .avatar-preview > div {
  width: 100%;
  height: 100%;
  border-radius: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  /* background-image: url("@/assets/add-image2.jpg") */
}
</style>
    