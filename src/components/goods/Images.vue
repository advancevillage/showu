<template>
    <div>
        <div v-bind:style="{'float': 'left', 'width': '40%'}">
            <Row v-bind:style="{marginBottom: '10px'}">
                <i-col span="6">
                    <span>{{languages.Images.main_front[language]}}</span>
                </i-col>
            </Row>
            <div class="upload_list" v-for="item in uploads.items" :key="item.uid">
                <template v-if="item.status === 'finished'">
                    <img :src="item.url">
                    <div class="upload_list_cover">
                        <Icon type="ios-eye-outline"></Icon>
                        <Icon type="ios-trash-outline"></Icon>
                    </div>
                </template>
                <template v-else>
                    <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                </template>
            </div>
            <Upload
                    ref="upload"
                    :show-upload-list="false"
                    :format="['jpg','jpeg','png']"
                    :max-size="2048"
                    :on-progress="handleUpload"
                    :on-success="uploadSuccess"
                    multiple
                    type="drag"
                    action="//jsonplaceholder.typicode.com/posts/"
                    style="display: inline-block;width:128px;">
                <div style="width: 128px;height:128px;line-height: 128px;">
                    <Icon type="ios-camera" size="128"></Icon>
                </div>
            </Upload>
        </div>
        <div v-bind:style="{'float': 'left', 'width': '40%'}">
            <Row v-bind:style="{marginBottom: '10px'}">
                <i-col span="6">
                    <span>{{languages.Images.main_back[language]}}</span>
                </i-col>
            </Row>
            <div class="upload_list" v-for="item in uploads.items" :key="item.uid">
                <template v-if="item.status === 'finished'">
                    <img :src="item.url">
                    <div class="upload_list_cover">
                        <Icon type="ios-eye-outline"></Icon>
                        <Icon type="ios-trash-outline"></Icon>
                    </div>
                </template>
                <template v-else>
                    <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                </template>
            </div>
            <Upload
                    ref="upload"
                    :show-upload-list="false"
                    :format="['jpg','jpeg','png']"
                    :max-size="2048"
                    :on-progress="handleUpload"
                    :on-success="uploadSuccess"
                    multiple
                    type="drag"
                    action="//jsonplaceholder.typicode.com/posts/"
                    style="display: inline-block;width:128px;">
                <div style="width: 128px;height:128px;line-height: 128px;">
                    <Icon type="ios-camera" size="128"></Icon>
                </div>
            </Upload>
        </div>
        <div v-bind:style="{'float': 'left', 'width': '100%'}">
            <Row v-bind:style="{marginBottom: '10px'}">
                <i-col span="6">
                    <span>{{languages.Images.minor[language]}}</span>
                </i-col>
            </Row>
            <div class="upload_list" v-for="item in uploads.items" :key="item.uid">
                <template v-if="item.status === 'finished'">
                    <img :src="item.url">
                    <div class="upload_list_cover">
                        <Icon type="ios-eye-outline"></Icon>
                        <Icon type="ios-trash-outline"></Icon>
                    </div>
                </template>
                <template v-else>
                    <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
                </template>
            </div>
            <Upload
                    ref="upload"
                    :show-upload-list="false"
                    :format="['jpg','jpeg','png']"
                    :max-size="2048"
                    :on-progress="handleUpload"
                    :on-success="uploadSuccess"
                    multiple
                    type="drag"
                    action="//jsonplaceholder.typicode.com/posts/"
                    style="display: inline-block;width:96px;">
                <div style="width: 96px;height:96px;line-height: 96px;">
                    <Icon type="ios-camera" size="96"></Icon>
                </div>
            </Upload>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Images",
        data() {
            return {
                languages: this.$languages,
                language: "chinese",
                uploads: {
                    items: [],
                }
            }
        },
        methods: {
            handleUpload: function(event, file, fileList) {
                this.uploads.items = fileList;
            },
            uploadSuccess (res, file) {
                console.log(res, file);
                file.url = 'https://o5wwk8baw.qnssl.com/7eb99afb9d5f317c912f08b5212fd69a/avatar';
                file.name = '7eb99afb9d5f317c912f08b5212fd69a';
            },
        }
    }
</script>

<style scoped>
    .upload_list {
        display: inline-block;
        width: 130px;
        height: 130px;
        text-align: center;
        line-height: 130px;
        border: 1px solid transparent;
        border-radius: 4px;
        overflow: hidden;
        background: #fff;
        position: relative;
        box-shadow: 0 1px 1px rgba(0,0,0,.2);
        margin-right: 4px;
    }
    .upload_list img{
        width: 100%;
        height: 100%;
    }
    .upload_list_cover{
        display: none;
        position: absolute;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
        background: rgba(0,0,0,.6);
    }
    .demo-upload-list:hover .upload_list_cover{
        display: block;
    }
    .upload_list_cover i{
        color: #fff;
        font-size: 20px;
        cursor: pointer;
        margin: 0 2px;
    }
</style>