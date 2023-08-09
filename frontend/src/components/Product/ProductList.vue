<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col text-left">
        <div class="">
          <h2>Listado de productos</h2>
          <b-button size="sm" :to="{name: 'NewProduct'}" variant="primary">
            Nuevo producto
          </b-button>
        </div>
        <br>
        <div class="col-md-12">
          <b-table striped hover :items="products" :fields="fields">

            <template slot="action" slot-scope="data">
              <b-button size="sm" variant="primary" :to="{ name:'EditProduct', params: {productId: data.item.id} }">
                Editar
              </b-button>
              <b-button size="sm" variant="danger" :to="{ name:'DeleteProduct', params: {productId: data.item.id} }">
                Eliminar
              </b-button>
            </template>

          </b-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data () {
    return {
      fields: [
        { key: 'nombre', label: 'Nombre' },
        { key: 'precio', label: 'Precio' },
        { key: 'descripcion', label: 'Descripción' },
        { key: 'action', label: '' }
      ],
      products: []
    }
  },
  methods: {

    getProducts () {
      const path = 'http://127.0.0.1:8000/all_product/'
      axios.get(path).then((response) => {
        this.products = response.data.allProducts
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },

  created(){
    this.getProducts()
  }
}
</script>

<style lang="css" scoped>
</style>
