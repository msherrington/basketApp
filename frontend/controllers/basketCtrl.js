const app = angular.module('basketApp', [])

app.controller('basketController', function (
    $http,
) {

    const self = this

    const init = async () => {
        self.itemExists = false
        self.djangoRestApi = 'http://localhost:8000/api'
        // await getItems()
        self.itemList = [{id:1, name: 'this'}, {id:2, name: 'that'}]
        self.orderItems = []
    }

    const getItems = async () => {
        await $http.get(self.djangoRestApi + '/item-list/').then(response => {
            self.itemList = response.data
        })
    }

    self.addItem = () => {
        self.itemExists = !self.itemExists
        // work out if the self.newItem is already in the orderitems
        // if it's not, add it
        // otherwise alert the user
    }

    // load all items
    // if item exists, attach it
    // else send a create request

    init()
})
