const app = angular.module('basketApp', [])

app.controller('basketController', function (
    $http,
) {

    const self = this

    const init = async () => {
        self.clearInput()
        self.clearAlert()
        self.djangoRestApi = 'http://localhost:8000/api'
        self.orderItems = []
        self.existingItemNames = []
        // self.itemList = await getItems()//{id:1, name: 'this'}, {id:2, name: 'that'}]
        // self.itemNames = self.itemList.map(item => item.name.toLowerCase())
    }

    const getItems = async () => {
        const response = await $http.get(self.djangoRestApi + '/items/')
        return response.data
    }

    self.addItem = () => {
        if (self.itemInput) {
            const lower = self.itemInput.toLowerCase()
            const formattedName = capitalize(self.itemInput)
            if (self.existingItemNames.includes(lower)) {
                self.existingItem = formattedName
                self.itemExists = true
            } else {
                const newItem = {
                    quantity: 1,
                    name: formattedName
                }
                self.orderItems.push(newItem)
                self.existingItemNames.push(lower)
            }
            self.clearInput()
        }
    }

    self.increase = item => {
        item.quantity++
    }

    self.decrease = item => {
        if (item.quantity > 1) {
            item.quantity--
        }
    }

    self.removeItem = item => {
        const index = self.orderItems.indexOf(item)
        if (index > -1) {
            self.orderItems.splice(index, 1);
        }
    }

    self.submit = () => {

    }

    self.clearAlert = () => {
        self.itemExists = false
    }

    self.clearInput = () => {
        self.itemInput = ''
    }

    const capitalize = name => {
        if (typeof name !== 'string') return name
        return name.charAt(0).toUpperCase() + name.slice(1)
    }

    // load all items
    // if item exists, attach it
    // else send a create request

    init()
})
