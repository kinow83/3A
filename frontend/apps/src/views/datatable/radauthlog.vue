<template>
	<div>
		<div class="content-section introduction">
			<div class="feature-intro">
				<h1>LOG <span>Authentication log</span></h1>
			</div>
		</div>

		<div class="content-section implementation">            
            <div class="card">
                <h5>Radauthlog</h5>
                <ProgressSpinner v-show="lazyloading['loading']" style="width:30px;height:30px" strokeWidth="8"/>
                <Button type="button" icon="pi pi-refresh" class="p-button-text" @click="getRadauthlog()"/>
                <DataTable :value="radauthlog" v-model:selection="selectedlog" selectionMode="single" dataKey="id" class="p-datatable-sm">
                    <Column field="user_id" header="UserID"></Column>
                    <Column field="username" header="Username"></Column>
                    <Column field="result" header="Result"></Column>
                    <Column field="reason" header="Reason"></Column>
                    <Column field="authdate" header="Date"></Column>
                </DataTable>
            </div>
		</div>
	</div>
</template>

<script>
import AAAService from '../../service/AAAService';

export default {
    data() {
        return {
            radauthlog: null,
            selectedlog: null,
            lazyloading: {"loading": false},
        }
    },
    AAAService: null,
    created() {
        this.AAAService = new AAAService(this.lazyloading);
    },
    mounted() {
        this.AAAService.getRadauthlog().then(data => this.radauthlog = data);
    },
    methods: {
        getRadauthlog() {
            this.AAAService.getRadauthlog().then(data => this.radauthlog = data);
        },
        onRowSelect(event) {
            this.$toast.add({severity: 'info', summary: 'Product Selected', detail: 'Name: ' + event.data.name, life: 3000});
        },
        onRowUnselect(event) {
            this.$toast.add({severity: 'warn', summary: 'Product Unselected', detail: 'Name: ' + event.data.name, life: 3000});
        }
    }
}
</script>