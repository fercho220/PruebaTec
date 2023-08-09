<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col">

        <h3>¿Estas seguro que deseas eliminar este producto?</h3>
        <p>Título : {{ element.nombre }}</p>
        <p>Descripción : {{ element.descripcion }}</p>

      </div>
    </div>

    <div class="row">
      <div class="col">
        <b-button v-on:click="deleteProduct" variant="danger">Eliminar</b-button>
      </div>
    </div>

  </div>

</template>

<script>
import axios from 'axios';
import swal from 'sweetalert'

export default {
  data () {
    return {
      productId: this.$route.params.productId,
      element: {
        nombre: '',
        descripcion: ''
      },
      allProducts: [],
    }
  },
  methods: {
    getProduct (){
      const path = `http://127.0.0.1:8000/all_product/`

      axios.get(path).then((response) => {
        this.allProducts = response.data.allProducts
        this.allProducts.forEach(product => {
          console.log('p',product)
        if (product.id === this.productId) {
          this.element.nombre = product.nombre;
          this.element.descripcion = product.descripcion;
          }
      })
      })
      .catch((error) => {
        console.log(error)
      })
    },
    deleteProduct () {
      const path = `http://127.0.0.1:8000/delete_product/${this.productId}/`

      axios.delete(path).then((response) => {
        location.href = '/products'
      })
      .catch((error) => {
        swal("No es posible eliminar el producto", "", "error")
      })
    }
  },
  created() {
    this.getProduct()
  }
}
</script>

<style lang="css" scoped>
</style>
