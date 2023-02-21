package adrien.com.isen.lafosse;

import io.quarkus.mongodb.panache.PanacheMongoRepository;

import javax.enterprise.context.ApplicationScoped;

@ApplicationScoped
public class PatientRepository implements PanacheMongoRepository<PatientEntity> {
}
