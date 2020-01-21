<template>
    <div>
        <Form :label-width="100">
            <FormItem :label="languages.Merchandise.category[language]">
                <Row>
                    <i-col span="20">
                        <Cascader :data="categories.items" change-on-select @on-change="handleCategory"></Cascader>
                    </i-col>
                </Row>
            </FormItem>
        </Form>
    </div>
</template>

<script>
    export default {
        name: "Category",
        data() {
            return {
                languages: this.$languages,
                language: "chinese",
                categories: {
                    items: [],
                    total: 0
                },
                status: 0x201,
            }
        },
        mounted: function() {
          this.QueryCategories();
        },
        methods: {
            //分类
            QueryCategories: async function() {
                const params = {
                    status: this.status,
                };
                const headers = {
                    "x-language": this.language
                };
                this.categories = await this.$api.QueryCategories(params, headers) || {total: 0, items: []};
                for(let i in this.categories.items) {
                    this.categories.items[i].value = this.categories.items[i].id;
                    this.categories.items[i].label = this.categories.items[i].name[this.language];
                    this.categories.items[i].children = [];
                }
                this.handleChildCategory(this.categories.items);
            },
            handleChildCategory: async function(items) {
                const headers = {
                    "x-language": this.language
                };
                items = items || [];
                if (items.length === 0) {
                    return
                }
                for (let i = 0; i < items.length; i++) {
                    let item = items[i];
                    let data = await this.$api.QueryChildCategories(item.id, {}, headers) || [];
                    for (let j in data) {
                        data[j].children = [];
                        data[j].value = data[j].id;
                        data[j].label = data[j].name[this.language];
                    }
                    item.children = data;
                    this.handleChildCategory(item.children);
                }
            },
            handleCategory(value, selectedData) {
                console.log(selectedData, value);
            },
        }
    }
</script>

<style scoped>

</style>