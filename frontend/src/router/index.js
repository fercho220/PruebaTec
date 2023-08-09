import Vue from 'vue'
import Router from 'vue-router'

import NewProduct from '@/components/Product/NewProduct'
import ProductList from '@/components/Product/ProductList'
import EditProduct from '@/components/Product/EditProduct'
import DeleteProduct from '@/components/Product/DeleteProduct'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/products',
      name: 'ProductList',
      component: ProductList
    },
    {
      path: '/products/new',
      name: 'NewProduct',
      component: NewProduct
    },
    {
      path: '/products/:productId/edit',
      name: 'EditProduct',
      component: EditProduct
    },
    {
      path: '/products/:productId/delete',
      name: 'DeleteProduct',
      component: DeleteProduct
    }
  ],
  mode: 'history'
})
