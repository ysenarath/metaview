<template>
    <div class="query-results-view" ref="QueryResultsView">
        <form class="query-input-form">
            <div class="form-group">
                <textarea v-model="query" type="text" class="form-control" placeholder="Search Query"></textarea>
            </div>
            <button type="button" class="btn btn-primary" v-on:click="submit">Submit</button>
        </form>
        <table class="table query-results-table">
            <thead>
            <tr>
                <th scope="col">Var</th>
                <th scope="col">Val</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in results">
                <td>{{ item.var }}</td>
                <td>{{ item.val }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        data: function () {
            return {query: '', results: []}
        },
        methods: {
            submit: function () {
                let query = encodeURIComponent(this.query);
                axios
                    .get('http://127.0.0.1:5000/api/v0.1/query?q="' + query + '"')
                    .then(response => {
                        this.results = [];
                        for (let i = 0; i < response.data.length; i++) {
                            let item = response.data[i];
                            for (const [key, value] of Object.entries(item)) {
                                this.results.push({'var': key, 'val': value});
                            }
                        }
                    });
            }
        }
    }
</script>

<style>
    .query-results-view {
        padding: 10px;
    }

    .query-input-form {
        padding: 5px;
    }

    .query-input-form > .form-group > textarea {
        min-height: 100px;
    }

    .query-results-table {
        margin-top: 10px;
        width: 100%;
        max-height: 100%;
        overflow-y: hidden;
    }
</style>