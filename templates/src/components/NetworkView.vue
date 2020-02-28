<template>
    <div class="network-view" ref="NetworkView"></div>
</template>


<script>
    import vis from 'vis-network';
    import axios from 'axios';

    export default {
        data: function () {
            return {nodes: [], edges: []}
        },
        methods: {
            update: function () {
                const data = {nodes: new vis.DataSet(this.nodes), edges: new vis.DataSet(this.edges)};
                const container = this.$refs.NetworkView;
                const options = {};
                const network = new vis.Network(container, data, options);
            }
        },
        mounted: function () {
            axios
                .get('http://127.0.0.1:5000/api/v0.1/predicates')
                .then(response => {
                    let predicates = response.data;
                    let temp = [];
                    this.edges = [];
                    for (let i = 0; i < predicates.length; i++) {
                        let item = predicates[i];
                        if (temp.indexOf(item.subject) === -1) {
                            temp.push(item.subject);
                        }
                        if (temp.indexOf(item.object) === -1) {
                            temp.push(item.object);
                        }
                        this.edges.push({from: item.subject, to: item.object, label: item.predicate});
                    }
                    this.nodes = [];
                    for (let i = 0; i < temp.length; i++) {
                        this.nodes.push({'id': temp[i], 'label': temp[i]});
                    }
                    this.update();
                });
        }
    };
</script>

<style type="text/css">
    .network-view {
        width: 100%;
        height: 100%;
        border: 1px solid white;
    }
</style>