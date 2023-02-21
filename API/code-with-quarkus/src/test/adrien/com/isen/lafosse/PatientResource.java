package adrien.com.isen.lafosse;

import org.bson.types.ObjectId;
import org.jboss.resteasy.annotations.jaxrs.PathParam;

import javax.inject.Inject;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.util.List;

@Path("/patients")
public class PatientResource {

    @Inject
    PatientRepository patientRepository;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<PatientEntity> getPatients() {
        return patientRepository.findAll().list();
    }

    @GET
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public PatientEntity getPatient(@PathParam("id") ObjectId id) {
        return patientRepository.findById(id);
    }
}
