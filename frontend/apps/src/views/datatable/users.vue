<template>
	<div>
		<div class="content-section introduction">
			<div class="feature-intro">
				<h1>Users</h1>
			</div>
		</div>

		<div class="content-section implementation">            
            <div class="card">
                <h5>Users</h5>  
                <DataTable :value="users" v-model:expandedRows="expandedRows" dataKey="user_id" class="p-datatable-sm" 
                    @row-expand="onRowExpand" @row-collapse="onRowCollapse">
                    <template #header>
                        <div class="table-header-container">
                            <ProgressSpinner v-show="lazyloading['loading']" style="width:30px;height:30px" strokeWidth="8"/>
                            <Button icon="pi pi-refresh" class="p-button-warning" label="Add" @click="openPosition('left')"/>
                            <Button icon="pi pi-refresh" class="p-button-success" @click="getUsers()"/>
                        </div>
                    </template>

                    <Column :expander="true" headerStyle="width: 3rem"/>
                    <Column headerStyle="width: 3rem">
                        <template #body="slotProps">
                        <i class="pi pi-user"></i>
                        </template>
                    </Column>
                    <Column field="user_id" header="UserID"></Column>
                    <Column field="username" header="Username"></Column>
                    <Column field="level" header="Lv"></Column>
                    <Column field="status" header="Status"></Column>
                    <Column field="email" header="E-mail"></Column>
                    <Column field="last_login" header="Logined"></Column>
                    
                    <template #expansion="slotProps">
                        <div class="orders-subtable">
                            <h5>Detail for {{slotProps.data.username}}</h5>
                            <div class="p-grid p-fluid">
                                <div class="p-col-12 p-md-3">
                                    <div class="p-inputgroup">
                                        <span class="p-inputgroup-addon">Created</span>
                                        <InputText v-model="slotProps.data.created" disabled />
                                    </div>
                                </div>
                                <div class="p-col-12 p-md-3">
                                    <div class="p-inputgroup">
                                        <span class="p-inputgroup-addon">Changed</span>
                                        <InputText v-model="slotProps.data.changed" disabled />
                                    </div>
                                </div>
                                <div class="p-col-12 p-md-3">
                                    <div class="p-inputgroup">
                                        <span class="p-inputgroup-addon">E-mail</span>
                                        <InputText v-model="slotProps.data.email" disabled />
                                    </div>
                                </div>
                                <div class="p-col-12 p-md-3">
                                    <div class="p-inputgroup">
                                        <span class="p-inputgroup-addon">Last logined</span>
                                        <InputText v-model="slotProps.data.last_login" disabled />
                                    </div>
                                </div>
                            </div>
                            <DataTable :value="slotProps.data.radauthlog">
                                <Column field="user_id" header="UserID" headerStyle="width: 15%"></Column>
                                <Column field="username" header="Username" headerStyle="width: 15%"></Column>
                                <Column field="result" header="Result" headerStyle="width: 15%"></Column>
                                <Column field="reason" header="Reason" headerStyle="width: 40%"></Column>
                                <Column field="authdate" header="Date" headerStyle="width: 15%"></Column>
                            </DataTable>
                            <div class="p-text-right p-p-3">
                                <Button label="Delete" class="p-button-danger" @click="click_delete_user(slotProps.data)"/>
                            </div>
                        </div>
                    </template>
                </DataTable>
            </div>
		</div>
        <Dialog header="Header" v-model:visible="displayPosition" :style="{width: '50vw'}" :position="position" :modal="true">
            <div class="p-fluid">
                <div class="p-col-12 p-md-4">
                    <div class="p-inputgroup">
                    <span class="p-inputgroup-addon">
                        <i class="pi pi-user"></i>
                    </span>
                        <InputText placeholder="UserID" v-model="popup_user_id" />
                    </div>
                </div>
                <div class="p-col-12 p-md-4">
                    <div class="p-inputgroup">
                        <span class="p-inputgroup-addon">
                            <i class="pi pi-user"></i>
                        </span>
                        <InputText placeholder="Username" v-model="popup_username" />
                    </div>
                </div>
                <div class="p-col-12 p-md-4">
                    <div class="p-inputgroup">
                        <span class="p-inputgroup-addon">P</span>
                        <Password v-model="popup_passwd" />
                    </div>
                </div>
                <div class="p-col-12 p-md-4">
                    <div class="p-inputgroup">
                        <span class="p-inputgroup-addon">E</span>
                        <InputText placeholder="E-mail" v-model="popup_email" />
                    </div>
                </div>
                <div class="p-col-12 p-md-4">
                    <div class="p-inputgroup">
                        <span class="p-inputgroup-addon">P</span>
                        <InputText placeholder="Phone" v-model="popup_phone" />
                    </div>
                </div>
            </div>
            <template #footer>
                <Button label="Yes" icon="pi pi-check" @click="click_add_user" autofocus />
                <Button label="No" icon="pi pi-times" @click="closePosition" class="p-button-text" />
            </template>
        </Dialog>
	</div>
</template>

<script>
import AAAService from '../../service/AAAService';

export default {
    data() {
        return {
            users: null,
            selected_user: null,
            lazyloading: {"loading": false},

            displayPosition: false,
            position: 'center',

            popup_user_id: null,
            popup_username: null,
            popup_passwd: null,
            popup_email: null,
            popup_phone: null,

            expandedRows: []

        }
    },
    AAAService: null,
    created() {
        this.AAAService = new AAAService(this.lazyloading);
    },
    mounted() {
        this.AAAService.getUsers().then(data => this.users = data);
    },
    methods: {
        click_delete_user(data) {
            this.AAAService.delUsers({
                user_id: data.user_id
            })
            .then(response => {
                this.getUsers()
                this.$toast.add({severity:'success', summary: 'Success Message', detail:'Success delete user '+data.user_id, life: 3000});                
            })
            .catch(error => {
                this.$toast.add({severity:'error', summary: 'Error Message', detail: error.response.data.result, life: 3000});
            });
        },
        click_add_user() {
            this.AAAService.setUsers({
                user_id: this.popup_user_id,
                username: this.popup_username,
                passwd: this.popup_passwd,
                email: this.popup_email,
                phone: this.popup_phone
            })
            .then(response => {
                this.closePosition()
                this.getUsers()
                this.$toast.add({severity:'success', summary: 'Success Message', detail:'Success add user '+this.popup_user_id, life: 3000});                
            })
            .catch(error => {
                this.$toast.add({severity:'error', summary: 'Error Message', detail: error.response.data.result, life: 3000});
            });
        },
        openPosition(position) {
            this.position = position;
            this.displayPosition = true;
        },
        closePosition() {
            this.displayPosition = false;
        },
        getUsers() {
            this.AAAService.getUsers().then(data => this.users = data);
        },
        onRowSelect(event) {
            this.$toast.add({severity: 'info', summary: 'User Selected', detail: 'Name: ' + event.data.username, life: 3000});
        },
        onRowUnselect(event) {
            this.$toast.add({severity: 'warn', summary: 'User Unselected', detail: 'Name: ' + event.data.username, life: 3000});
        },
        onRowExpand(event) {
            var params = {"user_id": event.data.user_id};
            this.AAAService.getRadauthlog(params).then(data => {
                var last = this.expandedRows[this.expandedRows.length-1]
                last.radauthlog = data;
            });
            this.$toast.add({severity: 'info', summary: 'User Expanded', detail: event.data.username, life: 3000});
        },
        onRowCollapse(event) {
            this.$toast.add({severity: 'success', summary: 'User Collapsed', detail: event.data.username, life: 3000});
        }
    }
}
</script>
<style scoped>
.p-button {
    margin: 0 .5rem 0 0;
    min-width: 10rem;
}
p {
    margin: 0;
}
.confirmation-content {
    display: flex;
    align-items: center;
    justify-content: center;
}
.p-dialog .p-button {
    min-width: 6rem;
}

.product-image {
    width: 100px;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23)
}
.orders-subtable {
    padding: 1rem;
}
</style>
