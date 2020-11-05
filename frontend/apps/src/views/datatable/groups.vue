<template>
	<div>
		<div class="content-section introduction">
			<div class="feature-intro">
				<h1>Groups</h1>
			</div>
		</div>

		<div class="content-section implementation">            
            <div class="card">
                <h5>Groups</h5>
                <div class="p-grid">
                    <div class="p-col">
                        <div class="table-header-container">
                            <ProgressSpinner v-show="lazyloading['loading']" style="width:30px;height:30px" strokeWidth="8"/>
                            <Button icon="pi pi-refresh" class="p-button-warning" label="Add" @click="openPosition('left')"/>
                            <Button icon="pi pi-refresh" class="p-button-success" @click="getGroups()"/>
                        </div>
                        <Tree :value="groups" :filter="true" filterMode="strict" selectionMode="single"  @node-select="onNodeSelect" @node-unselect="onNodeUnselect"></Tree>
                    </div>
                    <div class="p-col">
                        <div class="p-inputgroup">
                            <span class="p-inputgroup-addon">GroupID</span>
                            <InputText v-model="selected.group_id" />
                        </div>
                        <div class="p-inputgroup">
                            <span class="p-inputgroup-addon">GroupName</span>
                            <InputText v-model="selected.group_name" />
                        </div>
                        <div class="p-inputgroup">
                            <span class="p-inputgroup-addon">MacCheck</span>
                            <InputText v-model="selected.mac_check" />
                        </div>
                        <div class="p-inputgroup">
                            <span class="p-inputgroup-addon">vlanID</span>
                            <InputText v-model="selected.valn_id" />
                        </div>
                        <div class="p-inputgroup">
                            <span class="p-inputgroup-addon">Created</span>
                            <InputText v-model="selected.created" />
                        </div>
                        <div class="p-inputgroup">
                            <span class="p-inputgroup-addon">Changed</span>
                            <InputText v-model="selected.changed" />
                        </div>
                    </div>
                </div>
            </div>
            <div class="card">
                <h5>Users</h5>  
                <DataTable :value="users" v-model:expandedRows="expandedRows" dataKey="user_id" class="p-datatable-sm" 
                    @row-expand="onRowExpand" @row-collapse="onRowCollapse">
                    <template #header>
                        <div class="table-header-container">
                            <ProgressSpinner v-show="lazyloading['loading']" style="width:30px;height:30px" strokeWidth="8"/>
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
                        <InputText placeholder="GroupID" v-model="popup_group_id" />
                    </div>
                </div>
                <div class="p-col-12 p-md-4">
                    <div class="p-inputgroup">
                        <span class="p-inputgroup-addon">
                            <i class="pi pi-user"></i>
                        </span>
                        <InputText placeholder="GroupName" v-model="popup_group_name" />
                    </div>
                </div>
                <div class="p-col-12 p-md-4">
                    <div class="p-inputgroup">
                        <span class="p-inputgroup-addon">Vlan</span>
                        <InputText placeholder="Vlan-ID" v-model="valnid" />
                    </div>
                </div>
                <div class="p-col-12 p-md-4">
                    <h5>Mac Check</h5>
                    <div class="p-field-checkbox">
                        <Checkbox id="mac_check" v-model="mac_check" :binary="true" />
                        <label for="binary">{{mac_check}}</label>
                    </div>
                </div>

                <div class="p-col-12 p-md-4">
                    <div class="p-inputgroup">
                        <span class="p-inputgroup-addon">P</span>
                        <Dropdown v-model="selected.group_id" :options="group_list" optionLabel="group_name" :filter="true" placeholder="Select a Group" :showClear="true">
                            <template #value="slotProps">
                                <div class="country-item country-item-value" v-if="slotProps.value">
                                    <img src="../../assets/images/flag_placeholder.png" :class="'flag flag-' + slotProps.value.code.toLowerCase()" />
                                    <div>{{slotProps.value.group_name}}</div>
                                </div>
                                <span v-else>
                                    {{slotProps.placeholder}}
                                </span>
                            </template>
                            <template #option="slotProps">
                                <div class="country-item">
                                    <img src="../../assets/images/flag_placeholder.png" :class="'flag flag-' + slotProps.option.code.toLowerCase()" />
                                    <div>{{slotProps.option.group_name}}</div>
                                </div>
                            </template>
                        </Dropdown>
                    </div>
                </div>
            </div>
            <template #footer>
                <Button label="Yes" icon="pi pi-check" @click="click_add_group" autofocus />
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
            groups: null,
            lazyloading: {"loading": false},
            popup_group_id: null,
            popup_group_name: null,
            selected: {
                "group_id": null,
                "group_name": null,
            },
            group_list: [],
            mac_check: false,
            users: null,
            displayPosition: false,
            position: 'center',
            expandedRows: []

        }
    },
    AAAService: null,
    created() {
        this.AAAService = new AAAService(this.lazyloading);
    },
    mounted() {
        this.AAAService.getGroupsTree().then(data => this.groups = data);
    },
    methods: {
        click_delete_group(data) {
            this.AAAService.delGroups({
                group_id: data.group_id
            })
            .then(response => {
                this.getGroups()
                this.$toast.add({severity:'success', summary: 'Success Message', detail:'Success delete group '+data.group_id, life: 3000});                
            })
            .catch(error => {
                this.$toast.add({severity:'error', summary: 'Error Message', detail: error.response.data.result, life: 3000});
            });
        },
        click_add_group() {
            this.AAAService.setGroups({
                group_id: this.popup_group_id,
                group_name: this.popup_group_name,
            })
            .then(response => {
                this.closePosition()
                this.getGroups()
                this.$toast.add({severity:'success', summary: 'Success Message', detail:'Success add group '+this.popup_group_id, life: 3000});                
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
        getGroups() {
            this.AAAService.getGroupsTree().then(data => this.groups = data);
        },
        onNodeSelect(node) {
            //this.$toast.add({severity:'success', summary: 'Node Selected', detail: node.label, life: 3000});
            this.AAAService.getGroups({
                "group_id": node.group_id
            }).then(response => {
                if (response && response.length > 0) {
                    var data = response[0]
                    console.log(data);
                    this.selected.group_id = data.group_id;  
                    this.selected.group_name = data.group_name;
                    this.selected.mac_check = data.mac_check;
                    this.selected.vlan_id = data.vlan_ide;
                    this.selected.created = data.created;
                    this.selected.changed = data.changed;
                }
            });
            
            this.AAAService.getUsers({
                "group_id": node.group_id
            }).then(data => this.users = data);
        },
        onNodeUnselect(node) {
            this.$toast.add({severity:'success', summary: 'Node Unselected', detail: node.label, life: 3000});
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
