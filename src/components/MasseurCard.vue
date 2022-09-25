<template>
    <div class="masseur">
      <img src="@/assets/logo.png" style="max-width: 20px;max-height: 20px;"/>{{masseur.name}}
    </div>
</template>
  
<script>
  export default {

    name: 'MasseurCard',
    props: ['masseur'],
  }
</script>
<style>
.masseur {
  display:inline-block;
  flex-direction: column;
  align-items: center;
  border:1px solid;
  min-width: 300px;
  max-height: 200px;
  padding:10px;
}
.event-link {
  color: #2c3e50;
  text-decoration: none;
}
</style>

  